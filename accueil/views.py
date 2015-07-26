from aggregateur.views import aggregateur
from django.contrib import messages
from django.core.exceptions import ObjectDoesNotExist
from django.http import HttpResponseRedirect, HttpResponse, HttpRequest
from django.shortcuts import get_object_or_404, render, render_to_response, redirect

def accueil(request, page_number=1, fil=None):
	if request.user.is_authenticated() :
		return redirect('aggregateur')
	else :
		return render( request, 'empty_box.html', {
		'page_title': "Authentification",
			})