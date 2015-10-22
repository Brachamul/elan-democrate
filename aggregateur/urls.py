from django.conf.urls import patterns, url

from . import views

urlpatterns = patterns('',
	url(r'^$', views.aggregateur, name='aggregateur'),
	url(r'^(?P<page>[0-9]+)/$', views.aggregateur, name='aggregateur_page'),
	url(r'^nouveau/(?P<channel_slug>[a-z0-9-]+)$', views.nouveau_post, name='nouveau_post_avec_chaine'),
	url(r'^nouveau/$', views.nouveau_post, name='nouveau_post'),
	url(r'^comment/(?P<comment_id>[0-9]+)/vote/(?P<color>[A-Z]+)$', views.comment_vote, name='comment_vote'),
	url(r'^comment/(?P<comment_id>[0-9]+)/getcolor$', views.comment_color, name='comment_color'),
	url(r'^(?P<post_id>[0-9]+)/vote/(?P<color>[A-Z]+)$', views.vote, name='vote'),
	url(r'^(?P<post_id>[0-9]+)/pin/$', views.pin_post, name='pin_post'),
	url(r'^(?P<year>[0-9]+)-(?P<slug>[a-z0-9-]+)/comment/(?P<pk>[a-z0-9-]+)$', views.afficher_le_commentaire, name='commentaire'),
	url(r'^(?P<year>[0-9]+)-(?P<slug>[a-z0-9-]+)$', views.afficher_le_post, name='post'),
	url(r'^rank$', views.rank, name='rank'),
	url(r'^comment_medic$', views.comment_medic, name='comment_medic'),
)