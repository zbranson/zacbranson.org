from django.conf.urls import *
from django.conf import settings

urlpatterns = patterns('media.views',
    (r'^$', 'listMedia'),
    (r'^serve/([-\w]+)', 'serve'),
    (r'^delete/([-\w]+)', 'delMedia'),
	  (r'^upload/', 'upload'),
    (r'^download/([-\w]+)', 'download'),
    (r'^test/', 'test'),
)

