from piston.handler import BaseHandler
from api.models import Photo 
from django.utils import simplejson
from django.shortcuts import get_object_or_404
from piston.utils import rc

class PhotoHandler(BaseHandler):
    
    allowed_methods = ('GET')
    model = Photo
    # is this necessary? the id is needed in order to get dues
    exclude = ()

    def read(self, request, slug=None, photo=None):
        """
        Get photos
        """
        photos = Photo.objects
        if slug and photo:
            try:
                return photos.filter(destination__slug=slug).get(id=photo)
            except Photo.DoesNotExist:
                return rc.NOT_FOUND
        if slug:
            return photos.filter(destination__slug=slug)
        else:
            return photos.order_by('?')[:16]
