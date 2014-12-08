from django.conf.urls import patterns, url

from . import views

urlpatterns = patterns('',
    url(r'^televerser/$', views.televersement_du_fichier_adherent, name='televersement_du_fichier_adhérent'),
)