from django.shortcuts import render_to_response, get_object_or_404
from django.template import RequestContext
import urllib2
from django.utils import simplejson
from django.http import HttpResponseRedirect

# Create your views here.
def test(request):
    return render_to_response('test.html', context_instance=RequestContext(request))

def home(request):
    return render_to_response('home.html', context_instance=RequestContext(request))
