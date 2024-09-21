from django.db import models
from django.contrib.auth.models import AbstractUser, BaseUserManager
from django.utils import timezone
import datetime

# Create your models here

# User Manager

class CustomUserManager(BaseUserManager):
    def create_user(self, email, password=None, **fields):
        if not email:
            raise ValueError('The Email field must be set')
        email = self.normalize_email(email)
        user = self.model(email=email, **fields)
        if not password:
            raise ValueError("You must enter a valid password")
        else:
            user.set_password(password) # Hash password using set_password

        user.save(using=self._db) # Save user to database
        return user # return user

# User

class User(AbstractUser):
    email = models.EmailField(max_length=200, unique=True)  # Email field that must be unique
    username = models.CharField(
        max_length=150, 
        unique=True, # Make sure username is unique
        help_text='Required. 150 characters or fewer. Letters, digits, and spaces only.',
        validators=[],
        error_messages={
            'unique': "A user with that username already exists.",
        },
    ) 
    exp = models.PositiveIntegerField(default=0)  # Amount of exp user has
    level = models.PositiveIntegerField(default=1)  # Current level
    join_date = models.DateTimeField("date joined", default=timezone.now)

    objects = CustomUserManager()

    def is_new_user(self):
        # Check if the user has registered within the last 3 days
        return self.join_date >= timezone.now() - datetime.timedelta(days=3)

    def level_up(self):
        threshold = self.level * 100  # Amount of exp needed for user to level up (SCALES BY LEVEL)
        # If the user has enough exp to level up, increase level and carry over remaining exp
        if self.exp >= threshold:
            self.level += 1  # Increase level
            self.exp -= threshold  # Carry over excess EXP
            self.save()  # Update entry

    def __str__(self):
        return self.print_name()

