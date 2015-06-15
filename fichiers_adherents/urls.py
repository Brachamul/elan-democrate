from django.conf.urls import patterns, url

from . import views

urlpatterns = patterns('',
    url(r'^televerser/$', views.televersement, name='televersement_du_fichier_adhérent'),
    url(r'^(?P<fichier_id>[0-9]+)$', views.visualisation_du_fichier_adherent, name='visualisation_du_fichier_adherent'),
)