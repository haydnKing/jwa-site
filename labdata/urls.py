from django.conf.urls import patterns, url

from labdata import views

urlpatterns = patterns('',
		url(r'^$', views.home),
		url(r'^projects/(?:(?P<area>synbio|toxo|other)/)?$', views.projects,
			name='projects'),
		url(r'^projects/(?P<area>synbio|toxo|other)/(?P<slug>[\w-]+)/$', views.project,
			name='project'),
		url(r'^people/$', views.people, name='people'),
		url(r'^people/(?P<slug>[\w-]+)/$', views.person, name='person'),
	)
