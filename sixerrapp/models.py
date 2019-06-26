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

# parent class of Personal and Company
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    avatar = models.CharField(max_length=500)
    about = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    hashtags = models.ManyToManyField(Hashtag)

    def __str__(self):
        return self.user.username


class Company(models.Model):
    profile = models.OneToOneField(Profile, on_delete=models.CASCADE)
    title = models.CharField(max_length=500)
    url = models.TextField()  # career url


class Personal(models.Model):
    profile = models.OneToOneField(Profile, on_delete=models.CASCADE)
    resume = models.FileField(upload_to='resumes', null=True)

    companies = models.ManyToManyField(Company)  # for subscription to companies


# child class of Personal
class Recruiter(models.Model):
    personal = models.OneToOneField(Personal, on_delete=models.CASCADE)
    company = models.ForeignKey(Company, on_delete=models.CASCADE)


########################################

class Job(models.Model):
    title = models.CharField(max_length=500)
    companies = models.ForeignKey(Company, on_delete=models.CASCADE)
    description = models.TextField()
    requirement = models.TextField()
    url = models.TextField()
    hashtags = models.ManyToManyField(Hashtag)

    created_at = models.DateTimeField(auto_now_add=True)
    deadline = models.DateTimeField(blank=True, null=True)  # allow field to be blank and if so store as null

    def __str__(self):
        return self.title


class Story(models.Model):
    title = models.CharField(max_length=500)
    content = models.TextField()
    photo = models.FileField(upload_to='stories')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    # authors = models.ManyToManyField(User)  # enable when allow for a story to have many authors
    author = models.ForeignKey(User)

    companies = models.ManyToManyField(Company)  # featured companies
    hashtags = models.ManyToManyField(Hashtag)

    def __str__(self):
        return self.title

