from django.conf.urls import patterns, url

from labdata import views

urlpatterns = patterns('',
		url(r'^$', views.home),
		url(r'^about/$', views.about, name='about'),
		url(r'^themes/$', views.research_themes, name='research_themes'),
		url(r'^themes/(?P<slug>[\w-]+)/$', views.research_theme, name='research_theme'),
		url(r'^people/$', views.people, name='people'),
		url(r'^people/(?P<slug>[\w-]+)/$', views.person, name='person'),
		url(r'^resources/$', views.resources, name='resources'),
		url(r'^news/$', views.news, name='news'),
		url(r'^news/archive/$', views.news_archive, name='news_archive'),
		url(r'^news/(?P<year>\d{4})/(?P<month>\d{1,2})/(?P<day>\d+)/(?P<slug>[\w-]+)/$',
			views.news_item, name='news_item'),
		url(r'^funding/$', views.funding, name='funding'),
		url(r'^publications/$', views.publications, name='publications'),
	)
 
