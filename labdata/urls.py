from django.conf.urls import patterns, url

from labdata import views

urlpatterns = patterns('',
		url(r'^$', views.home),
		url(r'^projects/$', views.projects, name='projects'),
		url(r'^projects/(?P<slug>[\w-]+)/$', views.project, name='project'),
		url(r'^people/$', views.people, name='people'),
		url(r'^people/(?P<slug>[\w-]+)/$', views.person, name='person'),
		url(r'^resources/$', views.resources, name='resources'),
		url(r'^news/$', views.news, name='news'),
		url(r'^news/(?P<year>\d{4})/(?P<month>\d{1,2})/(?P<day>\d+)/(?P<slug>[\w-]+)/$',
			views.news_item, name='news_item'),
		url(r'^funding/$', views.funding, name='funding'),
		url(r'^funding/(?P<id>[\d]+)/$', views.funding_item, name='funding_item'),
		url(r'^publications/$', views.publications, name='publications'),
	)
 
urlpatterns += patterns('django.contrib.flatpages.views',
    url(r'^about/$', 'flatpage', {'url': '/about/'}, name='about'),
)  
