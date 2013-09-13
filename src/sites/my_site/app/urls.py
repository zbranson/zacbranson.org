from django.conf.urls import *

urlpatterns = patterns('app.views',
    (r'^$', 'index'),
    (r'^work/$', 'work'),
    (r'^education/$', 'education'),
    (r'^resume/$', 'resume'),
)
