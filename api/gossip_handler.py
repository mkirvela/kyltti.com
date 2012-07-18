from piston.handler import BaseHandler
from api.models import Gossip 
from django.utils import simplejson
from django.shortcuts import get_object_or_404
from piston.utils import rc

class GossipHandler(BaseHandler):
    
    allowed_methods = ('GET')
    model = Gossip
    # is this necessary? the id is needed in order to get dues
    exclude = ()

    def read(self, request):
        """
        Get latest gossips
        """
        gossips = Gossip.objects
        return gossips.all()
