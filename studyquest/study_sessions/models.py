from django.db import models
from django.utils import timezone
from users.models import User
import datetime

# Create your models here.

# Study Sessions

class StudySession(models.Model):
    user = models.ForeignKey(User, related_name='study_sessions', on_delete=models.CASCADE)
    start_time = models.DateTimeField(auto_now_add=True)
    end_time = models.DateTimeField(null=True, blank=True)

    def complete_study_session(self):
        if self.end_time is None:
            self.end_time = timezone.now()
            study_duration = (self.end_time - self.start_time).total_seconds() // 60  # Get duration in minutes
            exp_earned = int(study_duration / 10) * 5  # 5 EXP per 10 minutes of study
            self.user.exp += exp_earned
            self.user.save()
            self.save()

