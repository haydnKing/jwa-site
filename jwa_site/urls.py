from django.conf.urls import patterns, include, url

from labdata.admin import admin_site

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'jwa_site.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^admin/', include(admin_site.urls)),
		url(r'', include('labdata.urls')),
)

handler404 = '404.html'

