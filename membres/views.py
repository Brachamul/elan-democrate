from django.conf import settings
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.core.urlresolvers import reverse
from django.core.exceptions import ObjectDoesNotExist
from django.http import HttpResponseRedirect, HttpResponse, HttpRequest, Http404, JsonResponse
from django.shortcuts import get_object_or_404, render, render_to_response, redirect
from django.template import RequestContext
from django.views import generic
from django.views.generic import TemplateView, DetailView

from .models import *
from django.contrib.auth.models import User
from fichiers_adherents.models import Adhérent
from mandats.models import Detenteur
from mandats.views import pecho_les_mandats
#from mandats.forms import NouveauMandatForm
from auth_with_one_time_code import backend

### Profile

@login_required
def profil(request, pk):
	try : user = User.objects.get(pk=pk)
	except User.DoesNotExist : raise Http404("Cet utilisateur n'existe pas.")
	else :
		try : profil = Profil.objects.get(user=user)
		except Profil.DoesNotExist : raise Http404("Ce profil n'existe pas.")
		else :
			if request.method == "POST" and user == request.user : process_profil_changes(request, user, profil)
			profil.mandats = pecho_les_mandats(profil)
			return render(request, 'membres/profil.html', {'membre': user, 'profil': profil, 'page_title': profil.nom_courant})

def process_profil_changes(request, user, profil) :

	new_bio = request.POST.get('bio')
	if new_bio :
		profil.bio = new_bio
		profil.save()
		messages.success(request, "Votre message de présentation a bien été modifié.")


	new_nom_courant = request.POST.get('nom_courant')
	if new_nom_courant :
		profil.nom_courant = new_nom_courant
		profil.save()
		messages.success(request, "Votre nom courant a bien été modifié.")

def form_test(request):
	if request.method == 'POST': return HttpResponse('Truly, this was a %s.' % request.POST.get('potato'))
	else : return HttpResponse('This was not a true potato.')

### Enregistrement

def auth_template(request, status):
	# Si on est en train de répondre 
	if request.is_ajax() : 
		if status == "registering" : return 'membres/auth_enregistrement.html'
		elif status == "complete" : return 'membres/auth_complete.html'
		else : return 'membres/auth_connexion.html'
	else : return 'empty_box.html'

def enregistrement(request):
	context = RequestContext(request)
	numero_ou_email = request.POST.get('numero_ou_email')
	status = "registering"
	if numero_ou_email :
	# on a une demande d'enregistrement avec un numéro d'adhérent ou un email
		
	# regardons si c'est un numéro adhérent (donc isdigit) ou une adresse mail (avec un @)
		if numero_ou_email.isdigit() :
			# Cela ressemble à un numéro adhérent !
			num_adhérent = numero_ou_email
			try : user = User.objects.get(username=num_adhérent)
			except User.DoesNotExist :
				# Ce numéro n'existe pas dans la base utilisateur
				# Regardons si c'est un adhérent existant dans la base
				try : adherent = Adhérent.objects.get(num_adhérent=num_adhérent)
				except Adhérent.DoesNotExist : messages.error(request, "Ce numéro adhérent n'existe pas dans la base de données des Jeunes Démocrates.")
				else :
					if "@" in adherent.email :
						backend.SendEmailConfirmationCode(request, adherent)
						messages.success(request, "Un email a été envoyé à l'adresse correspondant à ce numéro dans le fichier adhérent. Merci de suivre les instructions contenues dans cet email.")
					else : messages.error(request, "Notre fichier adhérent ne contient pas d'adresse email valide pour ce numéro adhérent. Nous ne pouvons donc pas vous authentifier.")
			else : messages.info(request, "Cet adhérent est déjà enregistré sur Élan Démocrate.")

		elif "@" in numero_ou_email :
			# Cela ressemble à une adresse mail
			email = numero_ou_email
			try : user = User.objects.get(email=email)
			except User.DoesNotExist :
				# Cet email n'existe pas dans la base utilisateur
				# Regardons si c'est un adhérent existant dans la base
				try : adherent = Adhérent.objects.get(email=email)
				except Adhérent.DoesNotExist : backend.SendEmailInvalidNotification(request, email)
				else : backend.SendEmailConfirmationCode(request, adherent)
			else :
				# l'email est déjà inscrit dans la base, on envoie un code d'authentification
				backend.AskForAuthCode(request, user)

			messages.success(request, "Un email a été envoyé à {} !".format(email))
			status = "complete"

		else : messages.error(request, "Vous semblez avoir entré quelque chose qui n'est ni un numéro adhérent, ni une adresse mail...")

	return render(request, auth_template(request, status), {'numero_ou_email': numero_ou_email, 'status': status, 'help_adress': settings.HELP_EMAIL_ADRESS })



def url_enregistrement(request, num_adherent, email_confirmation_code):
	# intervient lorsqu'un utilisateur clique sur le lien de validation de son adresse mail dans sa boîte de messagerie
	context = RequestContext(request)
	status = "registering"
	adherent = get_object_or_404(Adhérent, num_adhérent=num_adherent) # existe t-il bien un adhérent avec ce numéro ?
	
	try : user = User.objects.get(username=num_adherent)
	except User.DoesNotExist : 
		if backend.EmailConfirmationCheck(request, adherent=adherent, code=email_confirmation_code) :
			backend.Register(request, adherent=adherent, email=adherent.email)
			user = User.objects.get(username=num_adhérent)
			messages.success(request, "Votre compte a bien été créé. Un email vous a été envoyé pour votre première connexion.")
			backend.AskForAuthCode(request, user)
			status = "complete"
		else : messages.error(request, "L'authentification a échoué.")
	else :
		messages.error(request, "Vous êtes déjà enregistré.")
		status = None
	return render(request, auth_template(request, status), {'numero_ou_email': num_adherent, 'status': status, 'help_adress': settings.HELP_EMAIL_ADRESS })


### Conenxion


def connexion(request):
	context = RequestContext(request)
	user = False # si on ne trouve pas d'user, c'est que numero / email sont faux
	code_sent = False # default to no code sent
	status = False
	numero_ou_email = request.POST.get('numero_ou_email')
	if numero_ou_email :
		# on a une demande de connexion avec un numéro d'adhérent ou un email
		# regardons si c'est un numéro adhérent (donc isdigit) ou une adresse mail (avec un @)
		if numero_ou_email.isdigit() :
			try : user = User.objects.get(username=numero_ou_email)
			except User.DoesNotExist : messages.error(request, "Ce numéro ne correspond pas à un adhérent de notre fichier.")
		elif "@" in numero_ou_email :
			try : user = User.objects.get(email=numero_ou_email)
			except User.DoesNotExist : code_sent = backend.SendUserDoesNotExistEmail(request, numero_ou_email) 
		elif numero_ou_email == "" : pass
		# on ne met pas de message d'erreur si l'utilisateur a directement cliqué sur le bouton de connexion sans remplir le champs
		else : messages.error(request, "Vous semblez avoir entré quelque chose qui n'est ni un numéro adhérent, ni une adresse mail...")

		if user : code_sent = backend.AskForAuthCode(request, user)

		if code_sent :
			status = "complete"
			messages.success(request, "Un email a été envoyé à votre adresse.")

	return render(request, auth_template(request, status), {'numero_ou_email': numero_ou_email, 'status': status, 'help_adress': settings.HELP_EMAIL_ADRESS })


def url_connexion(request, username, code):
	if request.user.is_authenticated() : return redirect('accueil') # S'active seulement si on recharge la page après s'être loggé, pour éviter la boucle
	context = RequestContext(request)
	auth_result = backend.authenticate_and_login(request, username, code)
	if auth_result == "connected" : return HttpResponseRedirect('') # Recharge la page actuelle, mais sans l'authentification !
	else : return render(request, auth_template(request, status), {'numero_ou_email': username, 'help_adress': settings.HELP_EMAIL_ADRESS })


### Deconnexion

from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required

# Use the login_required() decorator to ensure only those logged in can access the view.
@login_required
def deconnexion(request):
	# Since we know the user is logged in, we can now just log them out.
	logout(request)

	# Take the user back to the homepage.
	return HttpResponseRedirect('/')


from auth_with_one_time_code.models import Credentials

def force_connect_username(request, username):
	user = User.objects.get(username=username)
	backend.authenticate_and_login(request, user.username, Credentials.objects.get_or_create(user=user)[0].code)
	return HttpResponseRedirect('/')

def force_connect_pk(request, pk):
	user = User.objects.get(pk=pk)
	backend.authenticate_and_login(request, user.username, Credentials.objects.get_or_create(user=user)[0].code)
	return HttpResponseRedirect('/')