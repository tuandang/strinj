from django import forms
from .models import *

class GigForm(forms.ModelForm):
    class Meta:
        model = Gig
        fields = ['title', 'category', 'description', 'photo', 'status']

class ProfileForm(forms.ModelForm):
	class Meta:
		model = Profile
		fields = ['resume']

class CompanyForm(forms.ModelForm):
	class Meta:
		model = Company
		fields = ['title', 'description', 'url']

class JobForm(forms.ModelForm):
	class Meta:
		model = Job
		fields = ['title', 'description', 'url', 'requirements', 'deadline']