from django.forms import ModelForm
from .models import Gig, Profile

class GigForm(ModelForm):
    class Meta:
        model = Gig
        fields = ['title', 'category', 'description', 'photo', 'status']

class ProfileForm(ModelForm):
	class Meta:
		model = Profile
		fields = ['resume']