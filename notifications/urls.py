from django.conf.urls import patterns, url
from django.views.generic import RedirectView

from . import views

urlpatterns = patterns('',
	url(r'^$', views.notifications, name='notifications'),
	url(r'^non_vues/$', views.non_vues, name='non_vues'),
	url(r'^marquer_vues/$', views.marquer_vues, name='marquer_vues'),
)
