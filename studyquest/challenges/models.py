from django.db import models
from django.utils import timezone
from users.models import User
import datetime

# Create your models here.

# Challenges

class Challenge(models.Model):
    title = models.CharField(max_length=20)
    description = models.CharField(max_length=200)
    reward = models.PositiveIntegerField(default=50)
    date_created = models.DateTimeField("date created", default=timezone.now)

    def getTitle(self):
        return f"{self.title}"

    def getDesc(self):
        return f"{self.description}"

    def getReward(self):
        return f"{self.reward}"

    def isNewlyCreated(self):
        return self.date_created >= timezone.now() - datetime.timedelta(days=3)

# Challenge Steps

class ChallengeStep(models.Model):
    challenge = models.ForeignKey(Challenge, related_name='steps', on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    description = models.TextField(max_length=500)
    order = models.PositiveIntegerField()

    def __str__(self):
        return f"{self.challenge.title} - Step {self.order}: {self.title}"
       

# Challenge Progress

class UserChallengeProgress(models.Model):
    user = models.ForeignKey(User, related_name='challenge_progress', on_delete=models.CASCADE)
    challenge = models.ForeignKey(Challenge, related_name='user_progress', on_delete=models.CASCADE)
    completed_steps = models.PositiveIntegerField(default=0)  # Tracks number of steps completed
    is_completed = models.BooleanField(default=False)

    def completeStep(self):
        total_steps = self.challenge.steps.count()
        if self.completed_steps < total_steps:
            self.completed_steps += 1
            self.save()

        if self.completed_steps == total_steps:
            self.is_completed = True
            self.user.exp += self.challenge.exp_reward  # Reward EXP for completing the challenge
            self.user.save()
            self.save()



