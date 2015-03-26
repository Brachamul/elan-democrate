from django.conf.urls import patterns, url

from . import views

urlpatterns = patterns('',
	url(r'^$', views.all, name='aggregateur'),
	url(r'^nouveau/$', views.nouveau_post, name='nouveau_post'),
	url(r'^(?P<post_id>[0-9]+)/vote/(?P<color>[A-Z]+)$', views.vote, name='vote'),
#	url(r'^(?P<post_id>[0-9]+)/vote_neg$', views.vote_neg, name='vote_neg'),
	url(r'^(?P<slug>[a-z0-9-]+)$', views.afficher_le_post.as_view()),
)