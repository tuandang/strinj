from django.contrib import admin
from .models import Profile, Gig, Review, Company

# Register your models here..
admin.site.register(Profile)
admin.site.register(Gig)
admin.site.register(Review)
admin.site.register(Company)
