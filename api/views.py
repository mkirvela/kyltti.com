from django.shortcuts import render_to_response, get_object_or_404
#from django.template import RequestContext
#import urllib2
from django.utils import simplejson
from django.http import HttpResponse
from api.models import Gossip
from django.core import serializers

# Create your views here.
def news(request):
    #return HttpResponse(simplejson.dumps({'date': '2012-02-12', 'title': 'New gossip, oh my!', 'body': 'Nothing to see here, move along'}), mimetype='application/json')
    gossips = Gossip.objects.all().values('title', 'body', 'priority')
    #gossips = serializers.serialize("json", [Gossip.objects.all()], ensure_ascii=False)
    return HttpResponse(simplejson.dumps(gossips.__dict__), mimetype='application/json')
    #return HttpResponse(gossips, mimetype='application/json')
