from django.contrib import admin
from .models import *

# Register your models here..
admin.site.register(Hashtag)
admin.site.register(Industry)
admin.site.register(Sector)
admin.site.register(SkillOrTool)

# admin.site.register(Profile)
admin.site.register(Story)
admin.site.register(Company)
admin.site.register(Job)

admin.site.register(Personal)
admin.site.register(Recruiter)

admin.site.register(Feedback)