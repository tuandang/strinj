from __future__ import unicode_literals
from django.contrib.auth.models import User
from django.utils import timezone

from django.db import models

############################################
# Hashtag models


# parent class for Industry, Sector and SkillOrTool
# has Many to Many relationship w/ Industry, Sector, Skill or Tool, Story, Profile, Job
class Hashtag(models.Model):
    name = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name


class Industry(models.Model):
    hashtag = models.OneToOneField(Hashtag, on_delete=models.CASCADE)
    hashtags = models.ManyToManyField(Hashtag)


class Sector(models.Model):
    hashtag = models.OneToOneField(Hashtag, on_delete=models.CASCADE)
    hashtags = models.ManyToManyField(Hashtag)


class SkillOrTool(models.Model):
    hashtag = models.OneToOneField(Hashtag, on_delete=models.CASCADE)
    hashtags = models.ManyToManyField(Hashtag)

    # for query optimization
    industries = models.ManyToManyField(Industry)
    sectors = models.ManyToManyField(Sector)


#################################################
# User account models

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

########################################


class Story(models.Model):
    title = models.CharField(max_length=500)
    description = models.TextField()
    photo = models.FileField(upload_to='')

    author = models.ForeignKey(User)

    companies = models.ManyToManyField(Company)
    hashtags = models.ManyToManyField(Hashtag)

    create_time = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.title

class Job(models.Model):
    title = models.CharField(max_length=500)
    company = models.ForeignKey(Company, null=True, blank=True, on_delete=models.CASCADE)
    requirements = models.TextField() # TODO
    # TODO hashtag = 
    description = models.TextField()
    deadline = models.DateTimeField(null=True, default=timezone.now)
    url = models.TextField()
    hashtags = models.ManyToManyField(Hashtag)
