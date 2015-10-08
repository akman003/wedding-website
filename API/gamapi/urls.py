from django.conf.urls import patterns, include, url
from django.contrib import admin
from rest_framework import routers
from rsvps import views

admin.autodiscover()

urlpatterns = patterns('',

	# disabling RSVP URLs, since we are no longer accepting RSVPs:	
	url(r'^', include('rsvps.urls')),

    url(r'^admin/', include(admin.site.urls)),
    
)
