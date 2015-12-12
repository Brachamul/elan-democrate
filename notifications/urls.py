from django.conf.urls import patterns, url
from django.views.generic import RedirectView

from . import views

urlpatterns = patterns('',
	url(r'^$', views.notifications, name='notifications'),
	url(r'^number_of_unseen_notifications/$', views.number_of_unseen_notifications, name='number_of_unseen_notifications'),
	url(r'^mark_all_notifications_as_seen/$', views.mark_all_notifications_as_seen, name='mark_all_notifications_as_seen'),
	url(r'^notifyme/$', views.notifyme, name='notifyme'),
)
