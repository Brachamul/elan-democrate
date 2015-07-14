from django.conf.urls import patterns, url
from django.views.generic import RedirectView

from . import views
from . import models

urlpatterns = [
	url(r'^$', RedirectView.as_view(permanent=False, url='par_membre/'), name='mandats'),
	url(r'^par_membre/$', views.afficher_les_mandats, name='afficher_les_mandats'),
]
