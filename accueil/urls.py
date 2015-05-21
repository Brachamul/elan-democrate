from django.conf.urls import patterns, url
from django.views.generic.base import RedirectView

from . import views

urlpatterns = patterns('',
	url(r'^page:(?P<page_number>[0-9]+)$', views.accueil, name='accueil'),
	url(r'^$', RedirectView.as_view(permanent=False, url='/accueil/page:1')),
)
