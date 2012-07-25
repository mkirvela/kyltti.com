from piston.handler import BaseHandler
from api.models import Gossip 
from django.utils import simplejson
from django.shortcuts import get_object_or_404
from piston.utils import rc

class GossipHandler(BaseHandler):
    
    allowed_methods = ('GET')
    model = Gossip
    exclude = ()

    def read(self, request):
        """
        Get latest gossips
        """
        return Gossip.objects.all()
