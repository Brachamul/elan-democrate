from django.conf.urls import patterns, url

from . import views

urlpatterns = patterns('',
	url(r'^$', views.all, name='aggregateur'),
	url(r'^nouveau/$', views.nouveau_post, name='nouveau_post'),
	url(r'^(?P<post_id>[0-9]+)/vote/(?P<color>[A-Z]+)$', views.vote, name='vote'),
	url(r'^(?P<slug>[a-z0-9-]+)$', views.afficher_le_post, name='post'),
	url(r'^(?P<slug>[a-z0-9-]+)/c/(?P<pk>[a-z0-9-]+)$', views.afficher_le_commentaire, name='commentaire'),
	url(r'^rank_posts/$', views.rank_posts, name='rank_posts'),
)