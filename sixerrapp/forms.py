from django.forms import ModelForm
from .models import *

class GigForm(ModelForm):
    class Meta:
        model = Gig
        fields = ['title', 'category', 'description', 'photo', 'status']

class ProfileForm(ModelForm):
	class Meta:
		model = Profile
		fields = ['resume']

class CompanyForm(ModelForm):
	class Meta:
		model = Company
		fields = ['title', 'description', 'url']

# class JobForm(ModelForm):
# 	class Meta:
# 		model = Job
# 		fields = ['title', 'description', 'url', 'requiments']