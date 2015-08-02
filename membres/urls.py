from django.conf.urls import patterns, url
from django.views.generic import RedirectView

from . import views

urlpatterns = patterns('',
	url(r'^$', RedirectView.as_view(permanent=False, url='/accueil/'), name='membres'),
	url(r'^enregistrement/$', views.enregistrement, name='enregistrement'),
	url(r'^enregistrement/(?P<num_adherent>[\d]+)&(?P<email_confirmation_code>[A-Z0-9]+)$', views.url_enregistrement, name='url_enregistrement'),
	url(r'^connexion/$', views.connexion, name='connexion'),
	url(r'^connexion/(?P<username>[\d]+)&(?P<code>[A-Z0-9]+)$', views.url_connexion, name='url_connexion'),
	url(r'^deconnexion/$', views.deconnexion, name='deconnexion'),
	url(r'^force_connect/username/(?P<username>\d+)/$', views.force_connect_username),
	url(r'^force_connect/pk/(?P<pk>\d+)/$', views.force_connect_pk),
	url(r'^(?i)(?P<pk>\d+)/$', views.profil, name='profil'),	
)
