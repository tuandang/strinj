from django import forms
from .models import *

class StoryForm(forms.ModelForm):
    class Meta:
        model = Story
        fields = ['title', 'content', 'photo']

class ProfileForm(forms.ModelForm):
	class Meta:
		model = Personal
		fields = ['resume']

class CompanyForm(forms.ModelForm):
	class Meta:
		model = Company
		fields = ['title', 'profile', 'url']

class JobForm(forms.ModelForm):
	class Meta:
		model = Job
		fields = ['title', 'description', 'url', 'requirements', 'deadline']