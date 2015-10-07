from django.conf.urls import patterns, url

from . import views

urlpatterns = patterns('',
	url(r'^$', views.channel_list, name='public_channels'),
	url(r'^mes-chaines$', views.channel_list, {'channels': 'my-channels'}, name='my_channels'),
	url(r'^creer$', views.nouvelle_chaine, name='nouvelle_chaine'),
	url(r'^(?P<channel_slug>[\x00-\x7F]+)/rejoindre$', views.join_channel, name='join_channel'),
	url(r'^(?P<channel_slug>[\x00-\x7F]+)/quitter$', views.leave_channel, name='leave_channel'),
	url(r'^(?P<channel_slug>[\x00-\x7F]+)/candidats$', views.wanttojoin_channel, name='wanttojoin_channel'),
	url(r'^(?P<channel_slug>[\x00-\x7F]+)/autoriser/(?P<user_pk>\d+)$', views.allow_user_to_join_channel, name='allow_user_to_join_channel'),
	url(r'^(?P<channel_slug>[\x00-\x7F]+)/refuser/(?P<user_pk>\d+)$', views.deny_user_from_channel, name='deny_user_from_channel'),
	url(r'^(?P<channel_slug>[\x00-\x7F]+)$', views.aggregateur, name='chaine'),
)