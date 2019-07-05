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

class Gig(models.Model):
    CATEGORY_CHOICES = (
        ("GD", "Art & Design"),
        ("BFA", "Business, Finance & Accounting"),
        ("MS", "Math & Science"),
        ("ED", "Education"),
        ("IT", "Information Technology"),
    )

    title = models.CharField(max_length=500)
    category = models.CharField(max_length=2, choices=CATEGORY_CHOICES)
    description = models.TextField()
    photo = models.FileField(upload_to='gigs')
    status = models.BooleanField(default=True)
    user = models.ForeignKey(User)
    company = models.ManyToManyField(Company)
    create_time = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.title

class Job(models.Model):
    title = models.CharField(max_length=500)
    company = models.ForeignKey(Company, null=True, blank=True, on_delete=models.CASCADE)
    requirements = models.TextField() # TODO
    # TODO hashtag =
    description = models.TextField()
    deadline = models.DateTimeField(null=True, blank=True)
    url = models.TextField()