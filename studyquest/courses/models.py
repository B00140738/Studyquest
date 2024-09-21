from django.db import models
from django.utils import timezone
import datetime

# Create your models here.

# Courses

class Course(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField(max_length=500)
    exp_reward = models.PositiveIntegerField(default=100)  # EXP reward for completing the course

    def __str__(self):
        return self.title


# Course Progress

class UserCourseProgress(models.Model):
    user = models.ForeignKey(User, related_name='course_progress', on_delete=models.CASCADE)
    course = models.ForeignKey(Course, related_name='user_progress', on_delete=models.CASCADE)
    is_completed = models.BooleanField(default=False)

    def completeCourse(self):
        # Reward EXP for completing the course
        if not self.is_completed:
            self.is_completed = True
            self.user.exp += self.course.exp_reward # Add EXP
            # Update
            self.user.save() 
            self.save()



