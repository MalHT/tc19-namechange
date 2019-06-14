from project import settings
from django.db import models
from django.contrib.auth.models import User

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    location = models.CharField(max_length=30, blank=True)

class Task(models.Model):
    DONE = 3
    IN_PROGRESS = 2
    NOT_DONE = 1
    TASK_STATE = (
      (DONE, "Done"),
      (IN_PROGRESS, "In Progress"),
      (NOT_DONE, "Not Done"),
    )
    userid = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=200)
    body = models.CharField(max_length=200)
    parent = models.IntegerField(default=0)
    orgid = models.IntegerField(default=0)
    pub_date = models.DateTimeField('date published')
    state = models.IntegerField(choices=TASK_STATE)

class WikiPage(models.Model):
    name = models.CharField(max_length=200)
    body = models.CharField(max_length=2000)

class Organisation(models.Model):
    name = models.CharField(max_length=200)
    body = models.CharField(max_length=2000)
    contact = models.CharField(max_length=200)
    website = models.CharField(max_length=200)
    commontasks = models.CharField(max_length=200)
    
class Review(models.Model):
    POSITIVE = 1
    MIXED = 2
    NEGATIVE = 3
    RATING_CHOICES = (
      (POSITIVE, "Positive"),
      (MIXED, "Mixed"),
      (NEGATIVE, "Negative"),
    )
    orgid = models.ForeignKey(Organisation, on_delete=models.CASCADE)
    rating = models.IntegerField(choices=RATING_CHOICES)
    body = models.CharField(max_length=2000)
    userid = models.ForeignKey(User, on_delete=models.CASCADE)