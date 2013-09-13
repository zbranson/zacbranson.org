import urllib

from django.http import HttpResponseRedirect, Http404, HttpResponse
from django.shortcuts import render_to_response
from django.conf import settings
from django.views.decorators.csrf import csrf_exempt
from django.template import RequestContext

from google.appengine.ext import blobstore
#from google.appengine.api import memcache

from media import models
from gae_utils import blob_helper

def listMedia(request):
    list = models.Media.all()
    return render_to_response('media/medialist.html', {'list':list })

def delMedia(request, key):
    try:
        blob_key = str(urllib.unquote(key))
        media = models.Media.get(key)
        blobstore.delete(media.media.key())
        media.delete()
    except:
        return HttpResponseRedirect('/media/')
    return HttpResponseRedirect('/media/')


@csrf_exempt
def upload(request):
    blob_info = blob_helper.get_uploads(request, field_name='media', populate_post=True)
    if len(blob_info) == 1:
        media_item = models.Media(title='',
                           media=blob_info[0],
                           filename = blob_info[0].filename,
                           filesize = blob_info[0].size,
                           content_type = blob_info[0].content_type)
        media_item.save()
        #memcache.flush_all()
        return HttpResponseRedirect('/media/')
    return render_to_response(blob_info[0].key())

def serve(request, key):
    media = models.Media.get(key)
    return blob_helper.send_blob(request, media.media, save_as=False) 
                                                    
def download(request, key):
    media = models.Media.get(key)
    return blob_helper.send_blob(request, media.media, save_as=True)

def test(request):
  upload_url = blobstore.create_upload_url('/media/upload/')
  return render_to_response('media/test.html', {'upload_url': upload_url}, context_instance=RequestContext(request))
