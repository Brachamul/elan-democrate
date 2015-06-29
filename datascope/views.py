import logging
from django.conf import settings
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.core.exceptions import ObjectDoesNotExist
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.core.urlresolvers import reverse
from django.http import HttpResponseRedirect, HttpResponse, HttpRequest, Http404
from django.shortcuts import get_object_or_404, render, render_to_response, redirect
from django.template import RequestContext
from django.views import generic
from django.views.generic import TemplateView, DetailView

from fichiers_adherents.models import Adhérent
from membres.models import Profil
from mandats.models import Detenteur
from .models import *



@login_required
def fichier_adherents(request):
	detenteurs = Detenteur.objects.filter(profil = request.user.profil)
	if request.user.has_perm('gere_les_mandats') : adherents = Adhérent.objects.all()
	elif detenteurs :
		adherents = []
		for detenteur in detenteurs :
			if detenteur.actif() :
				federations_visibles = VueFederation.objects.filter(detenteur=detenteur)
				for federation in federations_visibles :
					adherents.append(federation.adherents())
	if adherents :
		print ("ADHERENTS:")
		print (adherents)
		return render(request, 'datascope/fichier_adherents.html', {
			'adherents': adherents,
			'page_title': "Fichier adhérents",
			})
	else :
		messages.error(request, "Vous n'avez pas accès au contenu du fichier adhérent.")
		return redirect('accueil')