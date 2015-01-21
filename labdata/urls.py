from django.conf.urls import patterns, url

from labdata import views

urlpatterns = patterns('',
		url(r'^$', views.home),
		url(r'^projects/$', 
			views.projects,
			name='projects'),
		url(r'^projects/(?P<slug>[\w-]+)/$', 
			views.project,
			name='project'),
		url(r'^people/$', views.people, name='people'),
		url(r'^people/(?P<slug>[\w-]+)/$', views.person, name='person'),
		url(r'^resources/$', views.resources, name='resources'),
		url(r'^publications/$', views.publications, name='publications'),
	)
 
urlpatterns += patterns('django.contrib.flatpages.views',
    url(r'^about/$', 'flatpage', {'url': '/about/'}, name='about'),
)  
