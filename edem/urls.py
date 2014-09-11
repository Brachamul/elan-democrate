from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.views.generic.base import RedirectView

urlpatterns = patterns('',
    url(r'^$', RedirectView.as_view(permanent=False, url='/accueil/')),
    url(r'^accueil/', include('accueil.urls'), name='accueil'),
    url(r'^fichier-adherent/', include('fichier-adhérent.urls'), name='fichier-adhérent'),
    url(r'^admin/', include(admin.site.urls)),
)