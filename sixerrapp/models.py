from __future__ import unicode_literals
from django.contrib.auth.models import User
from django.utils import timezone

from django.db import models

# Create your models here..
class Company(models.Model):
    title = models.CharField(max_length=500)
    description = models.TextField()
    url = models.TextField()
    time = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.title

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    avatar = models.CharField(max_length=500)
    resume = models.FileField(upload_to='resumes', null=True, blank=True)
    company = models.ForeignKey(Company, null=True, blank=True, on_delete=models.SET_NULL)

    def __str__(self):
        return self.user.username

class Story(models.Model):
    title = models.CharField(max_length=500)
    description = models.TextField()
    photo = models.FileField(upload_to='')

    author = models.ForeignKey(User)

    companies = models.ManyToManyField(Company)
    # hashtags = models.ManyToManyField(Hashtag)

    create_time = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.title

# class Feedback(models.Model):
    

class Job(models.Model):
    title = models.CharField(max_length=500)
    company = models.ForeignKey(Company, null=True, blank=True, on_delete=models.CASCADE)
    requirements = models.TextField() # TODO
    # TODO hashtag = 
    description = models.TextField()
    deadline = models.DateTimeField(null=True, default=timezone.now)
    url = models.TextField()

    def __str__(self):
        return self.title
