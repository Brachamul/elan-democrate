from django.contrib import messages
from django.core.urlresolvers import reverse
from django.core.exceptions import ObjectDoesNotExist
from django.http import HttpResponseRedirect, HttpResponse, HttpRequest, Http404
from django.shortcuts import get_object_or_404, render, render_to_response, redirect
from django.template import RequestContext
from django.views import generic
from django.views.generic.base import TemplateView

from django.contrib.auth.models import User



### Profile

class ProfileView(TemplateView):
	template_name = 'adherents/profil.html'

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
		# Attempt to grab information from the raw form information.
		# Note that we make use of both UserForm and UserProfileForm.
		user_form = UserForm(data=request.POST)

		if user_form.is_valid():
			# Save the user's form data to the database.
			user = user_form.save()

			# Now we hash the password with the set_password method.
			# Once hashed, we can update the user object.
			user.set_password(user.password)
			user.save()

			# Update our variable to tell the template registration was successful.
			registered = True
			messages.success(request, "You have successfully signed up!")

		# Invalid form or forms - mistakes or something else?
		# Print problems to the terminal.
		# They'll also be shown to the user.
		else:
			print (user_form.errors)

	# Render the template depending on the context.
	return render_to_response(
			'adherents/enregistrement.html',
			{'registered': registered},
			context)



### Connexion

from django.contrib.auth import authenticate, login
from django.http import HttpResponseRedirect, HttpResponse

def connexion(request):
	context = RequestContext(request)

	# If the request is a HTTP POST, try to pull out the relevant information.
	if request.method == 'POST':
		# Gather the username and password provided by the user.
		# This information is obtained from the login form.
		numero_adherent_ou_email = request.POST['numero_adherent_ou_email']
		adherent = numero_adherent_ou_email
		mot_de_passe = request.POST['mot_de_passe']

		# Use Django's machinery to attempt to see if the username/password combination is valid.
		# - a User object is returned if it is.
		user = authenticate(username=adherent, password=mot_de_passe)

		# If we have a User object, the details are correct.
		# If None (Python's way of representing the absence of a value), no user
		# with matching credentials was found.
		if user:
			# Is the account active? It could have been disabled.
			if user.is_active:
				# If the account is valid and active, we can log the user in.
				# We'll send the user back to the homepage.
				login(request, user)
				messages.success(request, "Vous êtes maintenant connecté.")
				return redirect('accueil')
			else:
				# An inactive account was used - no logging in!
				messages.error(request, "Votre compte est désactivé !")
		elif adherent == "" and mot_de_passe == "" :
			# On ne met pas de message d'erreur si l'utilisateur a directement cliqué sur le bouton de connexion sans écrire dans les champs
			pass
		else :
			# Bad login details were provided. So we can't log the user in.
			messages.error(request, "Vérifiez vos données, elles ne correspondent pas à un compte existant.")

		return render_to_response('adherents/connexion.html', {'username': numero_adherent_ou_email}, context)

	else :
		return render_to_response('adherents/connexion.html', {}, context)



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