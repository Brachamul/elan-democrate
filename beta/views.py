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
from django.contrib.auth.models import User
from membres.models import Profil

from .models import *
from .forms import *


def BetaSignupForm(request, email=False):
	if request.method == "POST":
		form = BetaForm(request.POST)
		success = processSignUp(request, form)
	else :
		if email: form = BetaForm(initial={'email': email})
		else: form = BetaForm()
		success = False
	return render(request, 'beta/form.html', {'form': form, 'page_title': 'Inscription à la Bêta', 'success': success })

def processSignUp(request, form):
	if form.is_valid():
		nouveau_candidat = form.save()
		messages.success(request, 'Votre inscription à la beta a bien été enregistrée !')
		return True
	else : return False

from django.contrib.admin.views.decorators import staff_member_required

@staff_member_required	
def beta_candidate_list(request):
	candidats = BetaCandidat.objects.all()
	return render(request, 'beta/list.html', {'objects': candidats, 'page_title': 'Liste des candidats à la Bêta'})

@staff_member_required	
def activate_beta_candidate(request, pk):
	candidat = get_object_or_404(BetaCandidat, pk=pk)
	new_user = User.objects.get_or_create(
		username=randomly_generated_digits(12),
		email=candidat.email.lower().strip(' '),
		)[0]
	profil = new_user.profil 
	profil.nom_courant = candidat.nom_courant
	profil.twitter = candidat.compte_twitter.strip('@').strip(' ')
	profil.save()
	candidat.converted = True
	candidat.save()
	SendBetaInvitation(new_user)
	messages.success(request, 'Le candidat a bien été ajouté.')
	return HttpResponseRedirect(reverse(beta_candidate_list))

import string, random
def randomly_generated_digits(i): return ''.join(random.SystemRandom().choice(string.digits) for _ in range(i))

# EMAIL

from django.core.mail import send_mail
from django.conf import settings
from django.contrib import messages

site_url = settings.SITE_URL
emailer = settings.EMAIL_HOST_USER

def SendBetaInvitation(user):
	send_mail(
		"[Élan Démocrate] Invitation à a Bêta",
		"Merci d'avoir postulé à la Bêta d'Élan Démocrate !\n\n"
		"Votre inscription a été validée, et vous pouvez désormais vous connecter :\n\n"
		"{lien}".format(lien=site_url),
		emailer,
		[user.email],
		fail_silently=False
		)
	return True
