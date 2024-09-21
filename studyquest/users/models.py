from django.db import models
from django.utils import timezone
import datetime

# Create your models here.

# Users

class User(models.Model):
    fname = models.CharField(max_length=20)
    lname = models.CharField(max_length=20)
    email = models.CharField(max_length=200, unique=True) # store email and make sure no duplicates are present
    password = models.CharField(max_length=200)
    exp = models.PositiveIntegerField(default=0) # Amount of exp user has
    level = models.PositiveIntegerField(default=1) # current level 
    join_date = models.DateTimeField("date joined", default=timezone.now)

    def printName(self):
        return f"{self.fname} {self.lname}"

    def isNewUser(self):
        # Check if the user has registered within the last 3 days
        return self.join_date >= timezone.now() - datetime.timedelta(days=3)

    def levelUp(self):
        threshold = self.level * 100 # Amount of exp needed for user to level up (SCALES BY LEVEL)
        # If the user has enough exp to level up, increase level and carry over remaining exp
        if self.exp >= threshold:
            self.level += 1 # Increase level
            self.exp = self.exp - threshold # Carry over excess EXP
            self.save() # update entry


