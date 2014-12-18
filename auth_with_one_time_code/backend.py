from django.contrib import messages

from django.contrib.auth.models import User



#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#

# Rules of the Auth :
hours_valid = 1
maximum_number_of_active_codes = 3

# Processing the rules
from datetime import datetime, timedelta
code_validity_threshold = datetime.now() - timedelta(hours=hours_valid)

def count_active_codes(user):
	return Credentials.objects.filter(user=user, date__lt=(code_validity_threshold)).count()


#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#


class OneTimeCodeBackend :
	
	def authenticate(self, username=None, code=None):
		user = User.objects.get(username=username)
		email = user.email
		credentials = Credentials.objects.filter(email=email, code=code)

		# look for credentials fitting email and code, but not older than the code validity threshold
		if credentials.filter(date__lt=(code_validity_threshold)).count() > 0 :
			return user
		else :
			if credentials.count() > 0 : messages.error(request, "Vos codes d'accès ont plus d'une heure et ne sont plus valides.")
			return None

	def get_user(self, user_id):
		try:
			return User.objects.get(pk=user_id)
		except User.DoesNotExist:
			return None



from django.core.mail import send_mail
from .models import Credentials

def SendAuthCode(user):
	new_credentials = Credentials(user=user, email=user.email)
	new_credentials.save()
	code = new_credentials.code
	lien = "http://elandemocrate.fr/adherent/connexion/" + user.username + "&" + code
	send_mail(
		"[Élan Démocrate] Code d'accès : {code}".format(code=code),
		"Cliquez sur le lien suivant {lien}, ou entrez le code {code} sur le site Élan Démocrate pour vous authentifier.\n\n"
		"Ce code d'accès ne sera valable qu'une fois.\n\n"
		"Les mots de passe sont fréquemment utilisés à plusieurs endroits sur internet. Il suffit qu'un seul des sites auxquels vous êtes inscrit soit piraté pour que votre mot de passe soit compromis. La méthode d'authentification utilisée ici, avec un code d'accès à utilisation unique, vous protège du vol de mot de passe.\n\n"
		"N'oubliez pas de changer souvent le mot de passe de votre boîte email !".format(code=code, lien=lien),
		'antonin.grele@gmail.com',
		[user.email],
		fail_silently=False
		)
	return True


def AskForAuthCode(request, user):
	if 0 < count_active_codes(user) < maximum_number_of_active_codes :
		messages.error(request, "Vous semblez avoir déjà reçu au moins un code, vérifiez votre boîte mail...")
		if SendAuthCode(user) :
			messages.success(request, "Un nouveau code d'accès vous a été envoyé par mail.")
	elif count_active_codes(user) >= maximum_number_of_active_codes :
		messages.warning(request, "Vous avez déjà reçu au moins 3 codes d'accès au cours de la dernière heure ! Vérifiez votre boîte mail...")
	else :
		if SendAuthCode(user) :
			messages.success(request, "Un code d'accès vous a été envoyé par mail.")
	return True # confirm that there is now an active code



