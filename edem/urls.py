from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.views.generic.base import RedirectView

urlpatterns = patterns('',
    url(r'^$', RedirectView.as_view(permanent=False, url='/accueil/')),
    url(r'^accueil/', include('accueil.urls'), name='accueil'),
    url(r'^fichiers-adherents/', include('fichiers_adhérents.urls'), name='fichiers_adhérents'),
    url(r'^admin/', include(admin.site.urls)),
)

from django.conf import settings
if settings.DEBUG:
    urlpatterns += patterns('',
        (r'^media/(?P<path>.*)$', 'django.views.static.serve', {
        'document_root': settings.MEDIA_ROOT}))
