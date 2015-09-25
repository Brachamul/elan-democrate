from django.conf.urls import patterns, url

from . import views

urlpatterns = patterns('',
	url(r'^$', views.channel_list, name='channels'),
	url(r'^(?P<slug>[\x00-\x7F]+)$', views.channel_details, name='channel'),
)