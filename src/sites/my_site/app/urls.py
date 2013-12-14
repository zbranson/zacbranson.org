from django.conf.urls import patterns, url

urlpatterns = patterns('app.views',
    url(r'^$', 'index', name='index'),
    url(r'^work/$', 'work', name='work'),
    url(r'^education/$', 'education', name='education'),
    url(r'^resume/$', 'resume', name='resume'),
)
