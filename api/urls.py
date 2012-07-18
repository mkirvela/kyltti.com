from django.conf.urls.defaults import *
from piston.resource import Resource
from django.http import HttpResponse
from piston.handler import AnonymousBaseHandler, BaseHandler
from api.gossip_handler import GossipHandler
from api.photo_handler import PhotoHandler
from api.destination_handler import DestinationHandler

gossip_handler = Resource(GossipHandler)
photo_handler = Resource(PhotoHandler)
destination_handler = Resource(DestinationHandler)

urlpatterns = patterns('',
   url(r'^news/$', gossip_handler),
   url(r'^destinations/$', destination_handler),
   url(r'^photos/$', photo_handler),
   url(r'^photos/(?P<slug>[^/]+)/$', photo_handler),
   url(r'^photos/(?P<slug>[^/]+)/(?P<photo>\d+)/$', photo_handler),
)
