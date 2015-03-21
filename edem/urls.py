from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.views.generic.base import RedirectView

admin.site.site_header = 'Élan Démocrate - Administration'

urlpatterns = patterns('',
	url(r'^$', RedirectView.as_view(permanent=False, url='/accueil/')),
	url(r'^accueil/', include('accueil.urls')),
	url(r'^membre/', include('membres.urls'), name='mon_profil'),
	url(r'^post/', include('aggregateur.urls')),
	url(r'^tableau-de-bord/', include('tableau_de_bord.urls')),
	url(r'^fichiers-adherents/', include('fichiers_adherents.urls'), name='fichiers_adherents'),
	url(r'^admin/', include(admin.site.urls)),
)

from django.conf import settings
if settings.DEBUG:
	urlpatterns += patterns('',
		(r'^media/(?P<path>.*)$', 'django.views.static.serve', {
		'document_root': settings.MEDIA_ROOT}))
