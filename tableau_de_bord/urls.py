from django.conf.urls import patterns, url

from . import views

urlpatterns = patterns('',
    url(r'^$', views.tableau_de_bord, name='tableau_de_bord'),
	url(r'^initialisation-edem/$', views.initialisation_edem, name='initialisation_edem'),
	url(r'^delete-all-mandates/$', views.delete_all_mandates, name='delete_all_mandates'),
)
