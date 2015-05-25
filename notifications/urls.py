from django.conf.urls import patterns, url

from . import views

urlpatterns = patterns('',
#	url(r'^$', views.toutes, name='notifications'),
	url(r'^json/(?P<filter>[a-z]+)$', views.json, name='notifications_json'),
)
