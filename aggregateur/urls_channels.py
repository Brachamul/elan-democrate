from django.conf.urls import patterns, url

from . import views

urlpatterns = patterns('',
	url(r'^$', views.channel_list, name='liste_des_chaines'),
	url(r'^creer$', views.nouvelle_chaine, name='nouvelle_chaine'),
	url(r'^(?P<channel_slug>[\x00-\x7F]+)$', views.aggregateur, name='chaine'),
)