from django.conf.urls import patterns, include, url

from labdata.admin import admin_site

from jwa_site import settings

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'jwa_site.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
		url(r'^tinymce/', include('tinymce.urls')),
    url(r'^admin/', include(admin_site.urls)),
		url(r'', include('labdata.urls', namespace='labdata')),
)

handler404 = '404.html'

if settings.DEBUG:
    urlpatterns += patterns('',
        url(r'^media/(?P<path>.*)$',
            'django.views.static.serve',
            {'document_root': settings.MEDIA_ROOT, }),
    )
