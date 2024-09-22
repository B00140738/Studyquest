from django.db import models
from django.contrib.auth.models import BaseUserManager
from django.utils import timezone
import datetime
from users.auth.hashers import UserPasswordHasherPBKDF2 # Import our custom password hasher
from django.contrib.auth.hashers import make_password
from django.core.exceptions import ValidationError
import re

# User Manager

class CustomUserManager(BaseUserManager):
    def create_user(self, username, name, email, password=None, **fields):
        if not username:
            raise ValueError("You must enter a username")
        if not name:
            raise ValueError("Please enter your full name")
        if not email:
            raise ValueError("The Email field must be set")
        email = self.normalize_email(email)
        user = self.model(username=username, name=name, email=email, **fields)
        if not password:
            raise ValueError("You must enter a valid password")
        else:
            user.set_password(password)  # Hash password using set_password
        user.save(using=self._db)  # Save user to database
        return user  # Return user

# User

class User(models.Model):
    email = models.EmailField(max_length=200, unique=True)  # Unique email field
    username = models.CharField(
        max_length=150,
        unique=True,
        help_text='Required. 150 characters or fewer. Letters, digits, and spaces only.',
        error_messages={
            'unique': "A user with that username already exists.",
        },
    )
    name = models.CharField(
        max_length=255,
        validators=[],
        help_text='Full name. Letters and spaces only. 255 characters or fewer.',
        error_messages={
            'max_length': "The name cannot exceed 255 characters.",
            'invalid_name': "Name must contain only letters and spaces."
        },
    )
    exp = models.PositiveIntegerField(default=0)  # User experience points
    level = models.PositiveIntegerField(default=1)  # User level
    join_date = models.DateTimeField("date joined", default=timezone.now)

    objects = CustomUserManager()

    def is_new_user(self):
        return self.join_date >= timezone.now() - datetime.timedelta(days=3)

    def level_up(self):
        threshold = self.level * 100  # EXP threshold to level up
        if self.exp >= threshold:
            self.level += 1
            self.exp -= threshold # Carry left over EXP into the next level
            self.save()

    def __str__(self):
        return self.username

    def clean(self):
        # Validate name
        if not re.match(r'^[a-zA-Z\s]+$', self.name):
            raise ValidationError("Name must contain only letters and spaces.")


