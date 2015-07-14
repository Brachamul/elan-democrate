from django.conf.urls import patterns, url
from django.views.generic import RedirectView

from . import views

urlpatterns = patterns('',
	url(r'^$', RedirectView.as_view(permanent=False, url='fichier_adherents/'), name='datascope'),
	url(r'^fichier_adherents/$', views.fichier_adherents, name='fichier_adherents'),
	url(r'^maj_federations/$', views.maj_federations, name='maj_federations'),
)
