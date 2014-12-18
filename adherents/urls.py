from django.conf.urls import patterns, url

from . import views

urlpatterns = patterns('',
	url(r'^enregistrement/$', views.enregistrement, name='enregistrement'),
	url(r'^connexion/$', views.connexion, name='connexion'),
	url(r'^connexion/(?P<username>[\d]+)&(?P<code>[A-Z0-9]+)$', views.url_connexion, name='url_connexion'),
	url(r'^deconnexion/$', views.deconnexion, name='deconnexion'),
	url(r'^(?i)(?P<username>\d+)/', views.ProfileView.as_view(), name='profile'),
)
