from django.core.exceptions import ObjectDoesNotExist
from django.contrib.auth.models import User
from django.contrib import messages
from django.conf import settings
from django.http import HttpResponseRedirect, HttpResponse, HttpRequest
from django.shortcuts import get_object_or_404, render, render_to_response
from django.template import RequestContext

import sys

from .models import *

def mandats_des_membres(request):
	membres = User.objects.all()
	for membre in membres :
		membre.mandats = pecho_les_mandats(membre)
	return render(request, 'mandats/mandats_des_membres.html', {'membres': membres})

def pecho_les_mandats(membre):
	membre.mandats = []
	try : mandats = Detenteur.objects.filter(user=membre)
	except Detenteur.DoesNotExist :
		membres.mandats = None
	else :
		for mandat in mandats : membre.mandats.append(mandat)
	return membre.mandats