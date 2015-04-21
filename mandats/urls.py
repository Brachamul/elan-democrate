from django.conf.urls import patterns, url
from django.views.generic import RedirectView

from . import views

urlpatterns = [
	url(r'^$', RedirectView.as_view(permanent=False, url='par_membre/'), name='mandats'),
	url(r'^par_membre/$', views.mandats_des_membres, name='mandats_des_membres'),
]
