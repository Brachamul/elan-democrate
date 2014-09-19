from django.shortcuts import get_object_or_404, render
from django.http import HttpResponseRedirect, HttpResponse, HttpRequest
from django.core.urlresolvers import reverse
from django.core.exceptions import ObjectDoesNotExist
from django.views import generic

from django.contrib.auth.models import User

from django.http import Http404

from django.views.generic.base import TemplateView

from towns.models import Player


### Profile

class ProfileView(TemplateView):

	template_name = 'profiles/profile.html'
 
	def get_context_data(self, **kwargs):

		context = super(ProfileView, self).get_context_data()

		user = get_object_or_404(User, username=self.kwargs['username']) # find the User instance with this username
		context['user_object'] = user

		try:
			player = Player.objects.filter(user=user, left=None).latest('joined') # finds the current player
			context['player'] = player
		except ObjectDoesNotExist:
			context['player'] = 'not_in_game' # for new players or people who just finished a game

		return context



### Signup

from django.template import RequestContext
from django.shortcuts import render_to_response
from .forms import UserForm

def signup(request):
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

		# Invalid form or forms - mistakes or something else?
		# Print problems to the terminal.
		# They'll also be shown to the user.
		else:
			print (user_form.errors)

	# Not a HTTP POST, so we render our form using two ModelForm instances.
	# These forms will be blank, ready for user input.
	else:
		user_form = UserForm()

	# Render the template depending on the context.
	return render_to_response(
			'profiles/signup.html',
			{'user_form': user_form, 'registered': registered},
			context)



### Login
from django.contrib.auth import authenticate, login
from django.http import HttpResponseRedirect, HttpResponse

def user_login(request):
	context = RequestContext(request)

	# If the request is a HTTP POST, try to pull out the relevant information.
	if request.method == 'POST':
		# Gather the username and password provided by the user.
		# This information is obtained from the login form.
		username = request.POST['username']
		password = request.POST['password']

		# Use Django's machinery to attempt to see if the username/password combination is valid.
		# - a User object is returned if it is.
		user = authenticate(username=username, password=password)

		# If we have a User object, the details are correct.
		# If None (Python's way of representing the absence of a value), no user
		# with matching credentials was found.
		if user:
			# Is the account active? It could have been disabled.
			if user.is_active:
				# If the account is valid and active, we can log the user in.
				# We'll send the user back to the homepage.
				login(request, user)
				return HttpResponseRedirect('/u/%s' % username)
			else:
				# An inactive account was used - no logging in!
				return HttpResponse("Your account is disabled, for some reason !")
		else:
			# Bad login details were provided. So we can't log the user in.
			print ("Invalid login details: {0}, {1}".format(username, password))
			return HttpResponse("Invalid login details supplied.")

	# The request is not a HTTP POST, so display the login form.
	# This scenario would most likely be a HTTP GET.
	else:
		# No context variables to pass to the template system, hence the
		# blank dictionary object...
		return render_to_response('profiles/login.html', {}, context)



### Logout
from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required

# Use the login_required() decorator to ensure only those logged in can access the view.
@login_required
def user_logout(request):
	# Since we know the user is logged in, we can now just log them out.
	logout(request)

	# Take the user back to the homepage.
	return HttpResponseRedirect('/')


### myprofile

from django.contrib.auth.models import User

def myprofile(request):
	if request.user.is_authenticated() :
		username = request.user.username
		return HttpResponseRedirect('/u/%s' % username)
	else :
		return HttpResponseRedirect('/u/login/')