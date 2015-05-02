from django.conf import settings
from django.contrib.auth.decorators import permission_required
from django.contrib.auth.models import User
from django.contrib import messages
from django.core.exceptions import ObjectDoesNotExist
from django.http import HttpResponseRedirect, HttpResponse, HttpRequest
from django.shortcuts import get_object_or_404, render, render_to_response
from django.template import RequestContext
from django.views.generic.edit import CreateView, UpdateView, DeleteView

import sys

from .models import *
from .forms import *

@permission_required('gère les mandats')
def afficher_les_mandats(request):
	profils = Profil.objects.all()
	for profil in profils :
		profil.mandats = pecho_les_mandats(profil)
	return render(request, 'mandats/afficher_les_mandats.html', {
		'profils': profils,
#		'nouveau_mandat_form': NouveauMandatForm()
		})

def pecho_les_mandats(profil):
	profil.mandats = []
	try : mandats = Detenteur.objects.filter(profil=profil)
	except Detenteur.DoesNotExist :
		profil.mandats = None
	else :
		for mandat in mandats : profil.mandats.append(mandat)
	return profil.mandats
