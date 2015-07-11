from aggregateur.views import aggregateur
from django.contrib import messages
from django.core.exceptions import ObjectDoesNotExist
from django.http import HttpResponseRedirect, HttpResponse, HttpRequest
from django.shortcuts import get_object_or_404, render, render_to_response, redirect

def accueil(request, page_number=1, fil=None):
	return render( request, 'accueil/accueil.html', {
		'message_accueil' : 'accueil/message_accueil.html',
		'aggregateur': aggregateur(request, page_number=page_number, fil=fil),
		'page_title': "Accueil",
		})