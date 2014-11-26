from django.conf.urls import patterns, url

from labdata import views

urlpatterns = patterns('',
		url(r'^$', views.home),
		url(r'^projects/(?:(?P<area>synbio|toxo)/)?$', views.projects),
		url(r'^people/$', views.people),
	)
