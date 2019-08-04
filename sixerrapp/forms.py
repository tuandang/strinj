from django import forms
from .models import *

class StoryForm(forms.ModelForm):
    class Meta:
        model = Story
        fields = ['title', 'description', 'photo'] # TODO: hashtags

class ProfileForm(forms.ModelForm):
	class Meta:
		model = Profile
		fields = []

class CompanyForm(forms.ModelForm):
	class Meta:
		model = Company
		fields = ['title', 'url']

# class FeedbackForm(forms.ModelForm):
# 	class Meta:
# 		model = Feedback
# 		fields = ['title', 'url']

class JobForm(forms.ModelForm):
	class Meta:
		model = Job
		fields = ['title', 'url', 'deadline']