from django.conf.urls import url
from sixerrapp import views

urlpatterns = [
    url(r'^$', views.home, name='home'),
    url(r'^gigs/(?P<id>[0-9]+)/$', views.gig_detail, name='gig_detail'),
    url(r'^my_gigs/$', views.my_gigs, name='my_gigs'),
    url(r'^create_gig/$', views.create_gig, name='create_gig'),
    url(r'^edit_gig/edit/(?P<id>[0-9]+)/$', views.edit_gig, name='edit_gig'),
    url(r'^profile/(?P<username>\w+)/$', views.profile, name='profile'),
    url(r'^checkout/$', views.create_purchase, name='create_purchase'),
]
