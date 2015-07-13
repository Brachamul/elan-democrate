from django.conf import settings
from django.contrib import messages
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User
from django.shortcuts import get_object_or_404, render, render_to_response, redirect

from .models import Credentials, EmailConfirmationInstance

#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#

# Rules of the Auth :
hours_code_valid_for_authentication = 1
maximum_number_of_active_authentication_codes = 3
maximum_number_of_attempts = 3
hours_code_valid_for_registration = 24

# Processing the rules
from datetime import timedelta
from django.utils import timezone

authentication_code_validity_threshold = timezone.now() - timedelta(hours=hours_code_valid_for_authentication)
registration_code_validity_threshold = timezone.now() - timedelta(hours=hours_code_valid_for_registration)

def count_active_authentication_codes(user):
	return Credentials.objects.filter(
		user=user,
		date__gt=(timezone.now() - timedelta(hours=hours_code_valid_for_authentication))).count()

def count_active_registration_codes(adherent):
	return EmailConfirmationInstance.objects.filter(
		adherent=adherent,
		date__gt=(timezone.now() - timedelta(hours=hours_code_valid_for_registration))).count()

#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#

site_url = settings.SITE_URL
emailer = settings.EMAIL_HOST_USER

#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#

class OneTimeCodeBackend :
	
	def authenticate(self, request, username=None, code=None):
		user = User.objects.get(username=username)
		email = user.email
		credentials = Credentials.objects.filter(email=email, code=code)

		for i in credentials :
			# pour éviter le forcing, on empêche plus de 3 essais par utilisateur et par heure
			i.attempts += 1
			i.save()

		if credentials.filter(date__gt=(authentication_code_validity_threshold)).count() > 0 :
			# look for credentials fitting email and code, but not older than x number of hours ago
			if credentials.filter(date__gt=(authentication_code_validity_threshold), attempts__lte=maximum_number_of_attempts).count() > 0 :
				return user
			else :
				messages.error(request, "Trop de tentatives d'accès ont été réalisées dernièrement, merci d'attendre avant de renouveller l'opération.")
				return None
		else :
			# s'il ya des codes valides mais trop vieux
			if credentials.count() > 0 :
				messages.error(request, "Vos codes d'accès ne sont plus valables.")
			return None

	def get_user(self, user_id):
		try:
			return User.objects.get(pk=user_id)
		except User.DoesNotExist:
			return None

def authenticate_and_login(request, username, code) :
	user = authenticate(request=request, username=username, code=code)
	if user :
		# Is the account active? It could have been disabled.
		if user.is_active :
			# If the account is valid and active, we can log the user in.
			# We'll send the user back to the homepage.
			login(request, user)
			messages.success(request, "Vous êtes maintenant connecté(e).")
			return "connected"
		else:
			# An inactive account was used - no logging in!
			messages.error(request, "Votre compte est désactivé !")
			return "inactive"
	else :
		# Bad login details were provided. So we can't log the user in.
		messages.error(request, "L'authentification n'a pas fonctionné.")
		return "bad-details"



from django.core.mail import send_mail

def SendAuthCode(user):
	new_credentials = Credentials(user=user, email=user.email)
	new_credentials.save()
	code = new_credentials.code
	lien = site_url + "/m/connexion/" + user.username + "&" + code
	send_mail(
		"[Élan Démocrate] Lien de connexion",
		"Cliquez sur le lien suivan pour vous authentifier: \n\n"
		"{lien}"
		"Ce code d'accès ne sera valable qu'une fois.\n\n"
		"Les mots de passe sont fréquemment utilisés à plusieurs endroits sur internet. Il suffit qu'un seul des sites auxquels vous êtes inscrit soit piraté pour que votre mot de passe soit compromis. La méthode d'authentification utilisée ici, avec un code d'accès à utilisation unique, vous protège du vol de mot de passe.\n\n"
		"N'oubliez pas de changer souvent le mot de passe de votre boîte email !".format(lien=lien),
		emailer,
		[user.email],
		fail_silently=False
		)
	return True

def DebugAuthCode(request, user):
	# only used for debugging purposes
	new_credentials = Credentials(user=user, email=user.email)
	new_credentials.save()
	code = new_credentials.code
	return code


def AskForAuthCode(request, user):
	active_codes = count_active_authentication_codes(user)
	if 0 < active_codes < maximum_number_of_active_authentication_codes :
		messages.warning(request, "Vous semblez avoir déjà reçu au moins un code, vérifiez votre boîte mail...")
		if SendAuthCode(user) :
			pass # messages.success(request, "Un nouveau code d'accès vous a été envoyé par mail.")
	elif active_codes >= maximum_number_of_active_authentication_codes : messages.error(request, "Vous avez déjà reçu {x} codes d'accès au cours de la dernière heure ! Vérifiez votre boîte mail...".format(x=active_codes))
	elif SendAuthCode(user) : messages.success(request, "Un code d'accès vous a été envoyé par mail.")
	return True # confirm that there is now an active code


def SendEmailConfirmationCode(request, adherent):
	# used to confirm that a user owns the adress before creating registering them
	# ! Check if there isn't already an active code for that person
	new_email_confirmation_instance = EmailConfirmationInstance(adherent=adherent, email=adherent.email)
	new_email_confirmation_instance.save()
	code = new_email_confirmation_instance.code
	lien = site_url + "/m/enregistrement/" + str(adherent.num_adhérent) + "&" + code
	send_mail(
		"[Élan Démocrate] Création de votre compte",
		"Bonjour,\n\n"
		"Sur le site Élan Démocrate, quelqu'un a effectué une demande de création de compte basée sur votre numéro adhérent, ou sur votre adresse email.\n\n"
		"Si vous êtes vous-même auteur de cette demande, cliquez sur le lien suivant pour finaliser la création de votre compte :\n\n{lien}\n\n"
		"Attention : votre adresse email est la clé de votre compte sur Élan Démocrate. Il est de votre responsabilité de vous prémunir contre la prise de contrôle de votre adresse email, en changeant notamment votre mot de passe de manière fréquente.\n\n"
		"À bientôt sur le réseau Élan Démocrate !\n\n".format(lien=lien),
		emailer,
		[new_email_confirmation_instance.email],
		fail_silently=False
		)
	return True

def EmailConfirmationCheck(request, adherent, code):
	# Vérifie que le code de confirmation d'une adresse mail est bon
	try : confirmation = EmailConfirmationInstance.objects.get(adherent=adherent, code=code)
	except EmailConfirmationInstance.DoesNotExist : messages.error(request, "Le code de confirmation est incorrect")
	else : return True

def SendEmailInvalidNotification(request, email):
	# Si l'adresse ne correspond pas à un adhérent, on ne peut pas créer le compte
	send_mail(
		"[Élan Démocrate] Votre adresse n'existe pas dans notre base adhérent",
		"Bonjour,\n\n"
		"Sur le site Élan Démocrate, une demande de création de compte basée sur votre adresse mail a été réalisée.\n\n"
		"Malheureusement, votre adresse n'existe pas dans notre base adhérent. Il est possible qu'elle n'ait pas été mise à jour dans le fichier des adhérents, ou qu'une autre erreur se soit produite.\n\n"
#		"Si vous êtes bien adhérent du Mouvement Démocrate de moins de 33 ans, cliquez sur le lien suivant pour obtenir de l'aide.\n\n{aide}\n\n"
#		"Sinon, vous pouvez adhérer au Mouvement Démocrate en cliquant ici : \n\n{adherer}\n\n"
		"Peut-être à bientôt, sur le réseau Élan Démocrate !\n\n", #.format(aide=?, adherer=?)
		emailer,
		[email],
		fail_silently=False
		)
	return True

def SendEmailAlreadyRegistered(request, email):
	# Si l'adresse correspond déjà à un adhérent
	lien = site_url + "/m/connexion/"
	send_mail(
		"[Élan Démocrate] Votre adresse mail est déjà associée à un compte",
		"Bonjour,\n\n"
		"Sur le site Élan Démocrate, une demande de création de compte basée sur votre adresse mail a été réalisée.\n\n"
		"Malheureusement, votre adresse est déjà associée à un compte sur Elan Démocrate.\n\n"
		"Vous pouvez vous connecter à ce compte en vous rendant ici :\n\n"
		"{lien}\n\n"
		"Peut-être à bientôt, sur le réseau Élan Démocrate !\n\n".format(lien=lien),
		emailer,
		[email],
		fail_silently=False
		)
	return True

def SendUserDoesNotExistEmail(request, email):
	# Si l'adresse ne correspond pas à un adhérent, on ne peut pas logger l'utilisateur
	lien = site_url + "/m/enregistrement/"
	send_mail(
		"[Élan Démocrate] Vous n'avez pas encore créé de compte",
		"Bonjour,\n\n"
		"Sur le site Élan Démocrate, une demande de connexion basée sur votre adresse mail a été réalisée.\n\n"
		"Malheureusement, votre adresse n'est pas encore associée à un compte.\n\n"
		"Si vous êtes adhérent jeune du Mouvement Démocrate, inscrivez-vous en vous rendant ici :\n\n"
		"{lien}\n\n"
#		"Sinon, vous pouvez adhérer au Mouvement Démocrate en cliquant ici : \n\n{adherer}\n\n"
		"Peut-être à bientôt, sur le réseau Élan Démocrate !\n\n".format(lien=lien),
		emailer,
		[email],
		fail_silently=False
		)
	return True

def Register(request, adherent, email) :
	new_user = User(username=adherent.num_adhérent, email=email)
	new_user.save()