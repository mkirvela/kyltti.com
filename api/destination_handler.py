from piston.handler import BaseHandler
from api.models import Destination 
from django.utils import simplejson
from django.shortcuts import get_object_or_404
from piston.utils import rc

class DestinationHandler(BaseHandler):
    
    allowed_methods = ('GET')
    model = Destination
    # is this necessary? the id is needed in order to get dues
    exclude = ()

    def read(self, request):
        """
        Get photos
        """
        destinations = Destination.objects
        return destinations.all()
