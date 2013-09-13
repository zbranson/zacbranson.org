import urllib
#from appengine_django.models import BaseModel
from google.appengine.ext import db
from django.db import models
from django.conf import settings

from django.http import HttpRequest

from google.appengine.ext import blobstore

class Media(db.Model):
    title = db.StringProperty()
    created = db.DateTimeProperty(auto_now_add=True)
    media = blobstore.BlobReferenceProperty()
    filename = db.StringProperty()
    filesize = db.IntegerProperty()
    content_type = db.StringProperty()

    def get_absolute_url(self):
        return '/media/serve/%s' % self.key()
        #return settings.SITE_URL+'/media/serve/%s' % self.key()

    def get_download_url(self):
        return '/media/download/%s' % self.key()
        
    def get_delete_url(self):
        return '/media/delete/%s' % self.key()
