from django.conf.urls import url
from sixerrapp import views
from django.contrib.auth.views import login

urlpatterns = [
    url(r'^$', views.home, name='home'),
    
    url(r'^gigs/(?P<id>[0-9]+)/$', views.gig_detail, name='gig_detail'),
    url(r'^my_gigs/$', views.my_gigs, name='my_gigs'),
    url(r'^create_gig/$', views.create_gig, name='create_gig'),
    url(r'^edit_gig/(?P<id>[0-9]+)/$', views.edit_gig, name='edit_gig'),
    
    url(r'^profile/(?P<username>\w+)/$', views.profile, name='profile'),
    url(r'^category/(?P<link>[\w|-]+)/$', views.category, name='category'),
    url(r'^search/$', views.search, name='search'),
    url(r'^register/$', views.register, name='register'),
    url(r'^login/$',
        login, {"template_name": "login_form.html"},
        name="login"),

    url(r'^register_company/$', views.register_company, name='register_company'),
    url(r'^edit_company/$', views.edit_company, name='edit_company'),
]

import os
# local
if 'BUCKETEER_AWS_ACCESS_KEY_ID' not in os.environ:
    from django.conf.urls.static import static
    from django.conf import settings
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)