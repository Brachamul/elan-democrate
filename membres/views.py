from django.contrib import messages
from django.core.urlresolvers import reverse
from django.core.exceptions import ObjectDoesNotExist
from django.http import HttpResponseRedirect, HttpResponse, HttpRequest, Http404
from django.shortcuts import get_object_or_404, render, render_to_response, redirect
from django.template import RequestContext
from django.views import generic
from django.views.generic.base import TemplateView

from .models import *
from django.contrib.auth.models import User
from fichiers_adherents.models import Adhérent

from auth_with_one_time_code import backend

### Card

def carte_profil(request):
	return {
		'profil': Profil.objects.get(user=request.user),
		'afficher': True,
		'template': "membres/carte_profil.html",
		}



### Profile

class ProfileView(TemplateView):
	template_name = 'membres/profil.html'

	def get_context_data(self, **kwargs):
		context = super(ProfileView, self).get_context_data()
		context['user_object'] = get_object_or_404(User, username=self.kwargs['username'])
		return context


### Enregistrement

from .forms import UserForm

def enregistrement(request):
	context = RequestContext(request)

	# A boolean value for telling the template whether the registration was successful.
	# Set to False initially. Code changes value to True when registration succeeds.
	registered = False

	# If it's a HTTP POST, we're interested in processing form data.
	if request.method == 'POST':
		numero_adherent_ou_email = request.POST.get('numero_adherent_ou_email')

		# regardons si c'est un numéro adhérent (donc isdigit) ou une adresse mail (avec un @)
		if numero_adherent_ou_email.isdigit() :
			num_adhérent = numero_adherent_ou_email
			# Cela ressemble à un numéro adhérent !
			try : user = User.objects.get(username=num_adhérent)
			except User.DoesNotExist :
				# Ce numéro n'existe pas dans la base utilisateur
				# Regardons si c'est un adhérent existant dans la base
				try : adherent = Adhérent.objects.get(num_adhérent=num_adhérent)
				except Adhérent.DoesNotExist : print("Ce numéro adherent n'existe pas dans la base de données des Jeunes Démocrates.")
				else :
					if "@" in adherent.email :
						print ("Envoi d'email de création de compte à ", adherent.email)
						backend.SendEmailConfirmationCode(request, adherent)
						messages.success(request, "Un email a été envoyé à l'adresse correspondant à ce numéro dans le fichier adhérent. Merci de suivre les instructions contenues dans cet email.")
					else :
						print ("Adresse email non valable : [", adherent.email, "]")
						messages.error(request, "Notre fichier adhérent ne contient pas d'adresse email valide pour ce numéro adhérent. Nous ne pouvons donc pas vous authentifier.")
			else : messages.info(request, "Cet adhérent est déjà enregistré sur Élan Démocrate.")

# !		elif "@" in numero_adherent_ou_email :
#			# Cela ressemble à une adresse mail
#			email = numero_adherent_ou_email
#			try : user = User.objects.get(email=email)
#			except User.DoesNotExist :
#				messages.error(request, "Nous ne connaissons pas cette adresse email.")
#			else : username = user.username
#		elif numero_adherent_ou_email == "" : pass
#		# on ne met pas de message d'erreur si l'utilisateur a directement cliqué sur le bouton de connexion sans remplir le champs
#		else : messages.error(request, "Vous semblez avoir entré quelque chose qui n'est ni un numéro adhérent, ni une adresse mail...")
#			user.save()
#			registered = True
#			messages.success(request, "Votre enregistrement est effectué !")

	return render_to_response(
			'membres/enregistrement.html',
			{'registering': True},
			context)



def url_enregistrement(request, num_adherent, email_confirmation_code):
	# intervient lorsqu'un utilisateur clique sur le lien de validation de son adresse mail dans sa boîte de messagerie
	context = RequestContext(request)
	registered = False
	try : adherent = Adhérent.objects.get(num_adhérent=num_adherent) # existe t-il bien un adhérent avec ce numéro ?
	except Adhérent.DoesNotExist : print("[Log] Impossible d'identifier l'adhérent dont le numéro est %d." % (num_adherent))
	else :
		if backend.EmailConfirmationCheck(request, adherent=adherent, code=email_confirmation_code) :
			backend.Register(request, adherent=adherent, email=adherent.email)
			user = User.objects.get(username=adherent.num_adhérent)
			registered = True
	if registered :
		messages.success(request, "Votre compte a bien été créé, vous pouvez désormais vous connecter.")
		return redirect(reverse('mon-profil'))
	else :
		return render_to_response(
			'membres/enregistrement.html',
			{'registering': True},
			context)


### Connexion

def connexion(request):
	context = RequestContext(request)

	if request.method == 'POST' :

		username = None # default to no username
		code_sent = False
		numero_adherent_ou_email = request.POST.get('numero_adherent_ou_email')
		# regardons si c'est un numéro adhérent (donc isdigit) ou une adresse mail (avec un @)
		if numero_adherent_ou_email.isdigit() :
			username = numero_adherent_ou_email
		elif "@" in numero_adherent_ou_email :
			email = numero_adherent_ou_email
			try : user = User.objects.get(email=email)
			except User.DoesNotExist :
				messages.error(request, "Nous ne connaissons pas cette adresse email.")
			else : username = user.username
		elif numero_adherent_ou_email == "" : pass
		# on ne met pas de message d'erreur si l'utilisateur a directement cliqué sur le bouton de connexion sans remplir le champs
		else : messages.error(request, "Vous semblez avoir entré quelque chose qui n'est ni un numéro adhérent, ni une adresse mail...")

		if request.POST.get('form_type') == "send_code" and username != None :
			# l'utilisateur demande l'envoi d'un code d'authentification
			try : user = User.objects.get(username=username)
			except User.DoesNotExist : messages.error(request, "Nous avons essayé de vous envoyer un code d'accès par mail, mais cela semble n'avoir pas fonctionné.")
			else : code_sent = backend.AskForAuthCode(request, user)

		elif request.POST.get('form_type') == "login" and username != None  :
			# l'utilisateur demande à être authentifié
			code = request.POST.get('code', False)
			if code == False : messages.error(request, "Merci d'entrer un code, ou d'en demander un nouveau.")
			else :
				auth_result = backend.authenticate_and_login(request, username, code)
				print("Auth result is : ", auth_result)
				if auth_result == "connected" :
					print("going connected")
					return HttpResponseRedirect('/')
				elif auth_result == "bad-details" :
					print("going bad-details")
					return render_to_response('membres/connexion.html', {'username': username, 'code_sent': True, 'logging_in': True}, context)
				else :
					print("going to shit")
					return render_to_response('membres/connexion.html', {'username': username, 'code_sent': False, 'logging_in': True}, context)

		return render_to_response('membres/connexion.html', {'username': username, 'code_sent': code_sent, 'logging_in': True}, context)

	return render_to_response('membres/connexion.html', {'logging_in': True}, context) # if something fails, reload page with messages

def url_connexion(request, username, code):
	context = RequestContext(request)
	if auth_result == "connected" :
		return HttpResponseRedirect('/')
	if auth_result == "bad-details" :
		return render_to_response('membres/connexion.html', {'username': username, 'code_sent': True, 'logging_in': True}, context)
	return render_to_response('membres/connexion.html', {'username': username, 'code_sent': False, 'logging_in': True}, context)



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


