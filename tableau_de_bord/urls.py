from django.conf.urls import patterns, url

from . import views

urlpatterns = patterns('',
    url(r'^$', views.tableau_de_bord, name='tableau_de_bord'),
)
