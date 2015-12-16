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
from fichiers_adherents.models import Adherent
from mandats.models import Detenteur
from mandats.views import pecho_les_mandats
#from mandats.forms import NouveauMandatForm
from auth_with_one_time_code import backend

from . import message_strings

### Enregistrement

def auth_template(request, status=False):
	# Si on est en train de répondre 
	if request.is_ajax() : 
		if status == "registering" : return 'auth/auth_enregistrement.html'
		elif status == "complete" : return 'auth/auth_complete.html'
		else : return 'auth/auth_connexion.html'
	else : return 'auth/authenticateur.html'

def signup_view(request):

	''' Asks the user for a valid authentication token : email or member number.
		Then, looks for a database member that fits the token.
		Finally, sends a registration code to the new user. '''

	status = 'registering'
	token = request.POST.get('numero_ou_email')

	if token :
		token = token.lower().strip(' ')
		member = lookup_member(request, token)
		if member and  "@" in member.email :
			backend.SendEmailConfirmationCode(request, member)
			messages.success(request, SUCCESS_EMAIL_SENT_TO_YOUR_ADRESS)
			status = "complete"
		elif member :
			messages.error(request, ERROR_NO_VALID_EMAIL_LINKED_TO_THIS_MEMBER)
			return False

	return render(request, auth_template(request, status), {'numero_ou_email': token, 'status': status, 'help_adress': settings.HELP_EMAIL_ADRESS })




def lookup_member(request, token):

	''' Looks for a database member that fits the token.
		Returns member if found, returns False otherwise. '''

	if token.isdigit() : # the token looks like a member number
		try :
			user = User.objects.get(username=token)
			# checks if a user account with this member number exists
		except User.DoesNotExist :
			try :
				member = Adherent.objects.get(num_adhérent=token)
				return member
				# otherwise, checks if database contains this member number
			except Adherent.DoesNotExist :
				messages.error(request, message_strings.ERROR_MEMBER_NUMBER_DOES_NOT_EXIST_IN_MEMBERS_DATABASE)
				return False
		else :
			messages.info(request, message_strings.INFO_MEMBER_NUMBER_ALREADY_REGISTERED)
			return False

	elif "@" in token : # the token looks like an email adress
		try :
			user = User.objects.get(email=token)
			# checks if a user account with this email number exists
		except User.DoesNotExist :
			try :
				member = Adherent.objects.get(email=token)
				return member
				# otherwise, checks if database contains this email adress
			except Adherent.DoesNotExist :
				backend.SendEmailInvalidNotification(request, token)
				messages.success(request, message_strings.SUCCESS_EMAIL_SENT_TO_YOUR_ADRESS)
				return False
		else :
			# user account exists for this adress, so a login code email is sent instead
			backend.AskForAuthCode(request, user)
			messages.success(request, message_strings.SUCCESS_EMAIL_SENT_TO_YOUR_ADRESS)
			return False

	else :	# doesn't look like anything at all
		messages.error(request, message_strings.ERROR_DOES_NOT_LOOK_LIKE_MEMBER_NUMBER_OR_EMAIL_ADRESS)
		return False






def confirm_signup_view(request, num_adherent, code):
	# intervient lorsqu'un utilisateur clique sur le lien de validation de son adresse mail dans sa boîte de messagerie
	context = RequestContext(request)
	status = "registering"
	adherent = get_object_or_404(Adherent, num_adhérent=num_adherent) # existe t-il bien un adhérent avec ce numéro ?
	
	try : user = User.objects.get(username=num_adherent)
	except User.DoesNotExist : 
		if backend.EmailConfirmationCheck(request, adherent=adherent, code=code) :
			backend.Register(request, adherent=adherent, email=adherent.email)
			user = User.objects.get(username=num_adherent)
			messages.success(request, "Votre compte a bien été créé. Un email vous a été envoyé pour votre première connexion.")
			backend.AskForAuthCode(request, user)
			status = "complete"
		else : messages.error(request, "L'authentification a échoué.")
	else :
		messages.error(request, "Vous êtes déjà enregistré.")
		status = None
	return render(request, auth_template(request, status), {'numero_ou_email': num_adherent, 'status': status, 'help_adress': settings.HELP_EMAIL_ADRESS })


### Conenxion


def login_view(request):
	context = RequestContext(request)
	user = False # si on ne trouve pas d'user, c'est que numero / email sont faux
	code_sent = False # default to no code sent
	status = False
	numero_ou_email = request.POST.get('numero_ou_email')
	if numero_ou_email :
		numero_ou_email = numero_ou_email.lower().strip(' ')
		# on a une demande de connexion avec un numéro d'adhérent ou un email
		# regardons si c'est un numéro adhérent (donc isdigit) ou une adresse mail (avec un @)
		if numero_ou_email.isdigit() :
			try : user = User.objects.get(username=numero_ou_email)
			except User.DoesNotExist : messages.error(request, "Aucun compte n'est lié à ce numéro d'adhérent. Avez-vous déjà créé un compte ?")
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


def confirm_login_view(request, username, code):
	if request.user.is_authenticated() : return redirect('accueil') # S'active seulement si on recharge la page après s'être loggé, pour éviter la boucle
	auth_result = backend.authenticate_and_login(request, username, code)
	if auth_result == "connected" :return HttpResponseRedirect('') # Recharge la page actuelle, mais sans l'authentification !
	else : return render(request, auth_template(request), {'numero_ou_email': username, 'help_adress': settings.HELP_EMAIL_ADRESS })


### Deconnexion

from django.contrib.auth import logout

def logout_view(request):
	logout(request)
	# Take the user back to the homepage.
	return HttpResponseRedirect('/')


# Force connections when DEBUG = True

from auth_with_one_time_code.models import Credentials

def force_connect_username(request, username):
	if settings.DEBUG :
		user = User.objects.get(username=username)
		Credentials.objects.filter(user=user).delete()
		backend.authenticate_and_login(request, user.username, Credentials.objects.get_or_create(user=user)[0].code)
	else : messages.success(request, "Cette fonctionnalité n'est pas active en production.")
	return HttpResponseRedirect('/')

def force_connect_pk(request, pk):
	if settings.DEBUG :
		user = User.objects.get(pk=pk)
		Credentials.objects.filter(user=user).delete()
		backend.authenticate_and_login(request, user.username, Credentials.objects.get_or_create(user=user)[0].code)
	else : messages.success(request, "Cette fonctionnalité n'est pas active en production.")
	return HttpResponseRedirect('/')
