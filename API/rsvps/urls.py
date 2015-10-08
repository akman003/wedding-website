from django.conf.urls import patterns, url
from rest_framework.urlpatterns import format_suffix_patterns

urlpatterns = patterns('rsvps.views',
    url(r'^rsvps/search/(?P<query>\w+)$', 'invitee_search'),
    url(r'^rsvps/(?P<pk>[0-9]+)$', 'invitee_detail'),
)

urlpatterns = format_suffix_patterns(urlpatterns)
