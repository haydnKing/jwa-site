from django.conf.urls import patterns, url

from labdata import views

urlpatterns = patterns('',
		url(r'^$', views.home),
	)
