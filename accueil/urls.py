from django.conf.urls import patterns, url
from django.views.generic.base import RedirectView

from . import views

urlpatterns = patterns('',
	url(r'^page:(?P<page_number>[0-9]+)$', views.accueil),
	url(r'^$', views.accueil, name='accueil'),
)
