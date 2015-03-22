from django.conf.urls import patterns, url

from . import views

urlpatterns = patterns('',
	url(r'^$', views.all, name='aggregateur'),
	url(r'^nouveau/$', views.nouveau_post, name='nouveau_post'),
)
