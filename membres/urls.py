from django.conf.urls import patterns, url
from django.views.generic import RedirectView

from . import views

urlpatterns = patterns('',
	url(r'^$', RedirectView.as_view(permanent=False, url='/accueil/'), name='membres'),
	url(r'^(?i)(?P<pk>\d+)/$', views.profil, name='profil'),
)
