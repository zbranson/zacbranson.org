# Create your views here.
from django.shortcuts import get_object_or_404, render_to_response
from django.http import HttpResponseRedirect, HttpResponse
from django.core.urlresolvers import reverse
from django.template import RequestContext

def index(request):
  return render_to_response('app/about.html', {"page":"home"}, context_instance=RequestContext(request))

def work(request):
  return render_to_response('app/work.html', {"page":"work"}, context_instance=RequestContext(request))

def resume(request):
  return render_to_response('app/resume.html', {"page":"resume"}, context_instance=RequestContext(request))

def education(request):
  return render_to_response('app/education.html', {"page":"education"}, context_instance=RequestContext(request))

def facebook(request):
  return render_to_response('app/facebook.html', {"page":"work"}, context_instance=RequestContext(request))

def handler_500(request):
    r = render_to_response('500.html', context_instance=RequestContext(request))
    r.status_code = 500
    return r


def handler_404(request):
    r = render_to_response('404.html', context_instance=RequestContext(request))
    r.status_code = 404
    return r