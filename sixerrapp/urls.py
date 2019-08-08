from django.conf.urls import url
from sixerrapp import views
from django.contrib.auth.views import login

urlpatterns = [
    url(r'^$', views.home, name='home'),
    
    url(r'^stories/(?P<id>[0-9]+)/$', views.story_detail, name='story_detail'),
    url(r'^my_stories/$', views.my_stories, name='my_stories'),
    url(r'^create_story/$', views.create_story, name='create_story'),
    url(r'^edit_story/(?P<id>[0-9]+)/$', views.edit_story, name='edit_story'),
    
    url(r'^profile/(?P<username>\w+)/$', views.profile, name='profile'),
    url(r'^create_profile/$', views.create_profile, name='create_profile'),

    url(r'^search/$', views.search, name='search'),
    url(r'^register/$', views.register, name='register'),
    url(r'^login/$',
        login, {"template_name": "login_form.html"},
        name="login"),

    url(r'^register_company/$', views.register_company, name='register_company'),
    url(r'^edit_company/$', views.edit_company, name='edit_company'),

    url(r'^create_feedback/$', views.create_feedback, name='create_feedback'),

    url(r'^create_job/$', views.create_job, name='create_job'),
    url(r'^edit_job/(?P<id>[0-9]+)/$', views.edit_job, name='edit_job'),
    url(r'^view_job/(?P<id>[0-9]+)/$', views.view_job, name='view_job'),
]

import os
# local
if 'BUCKETEER_AWS_ACCESS_KEY_ID' not in os.environ:
    from django.conf.urls.static import static
    from django.conf import settings
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)