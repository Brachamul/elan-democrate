from django.conf.urls import patterns, url
from django.views.generic import RedirectView

from . import views

urlpatterns = patterns('',
	url(r'^enregistrement/$', views.signup_view, name='signup'),
	url(r'^enregistrement/(?P<num_adherent>[\d]+)&(?P<code>[A-Z0-9]+)$', views.confirm_signup_view, name='confirm_signup'),
	url(r'^connexion/$', views.login_view, name='login'),
	url(r'^connexion/(?P<username>[\d]+)&(?P<code>[A-Z0-9]+)$', views.confirm_login_view, name='confirm_login'),
	url(r'^deconnexion/$', views.logout_view, name='logout'),
	url(r'^force_connect/username/(?P<username>\d+)/$', views.force_connect_username),
	url(r'^force_connect/pk/(?P<pk>\d+)/$', views.force_connect_pk),
	)
