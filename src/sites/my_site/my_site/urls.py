from django.conf.urls import *
from django.conf import settings
from django.http import HttpResponse
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

handler500 = 'app.views.handler_500'
handler404 = 'app.views.handler_404'

urlpatterns = patterns('',
    # Example:
    url(r'^', include('app.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # (r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^sheriff/', include(admin.site.urls)),
)

urlpatterns += patterns('',
    url(r'^assets/(?P<path>.*)$', 'django.views.static.serve', {'document_root': settings.MEDIA_ROOT, 'show_indexes':False}),)

urlpatterns += patterns('',
    url(r'^robots\.txt$', lambda r: HttpResponse("User-agent: *\nDisallow: ", mimetype="text/plain")),
)

urlpatterns += patterns('',
    url(r'^static/(?P<path>.*)$', 'django.views.static.serve', {'document_root': settings.STATIC_ROOT, 'show_indexes':False}
    ),
)

urlpatterns += staticfiles_urlpatterns()
