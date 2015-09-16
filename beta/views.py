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

from .models import *
from .forms import *


def BetaSignupForm(request):
	if request.method == "POST": processSignUp()
	else : return render(request, 'beta/form.html', {'form': BetaForm(), 'page_title': 'Inscription à la Bêta', })

def processSignup():
	pass
	text_data = link_data = None # les données seront renvoyées au formulaire en cas d'erreur, pour éviter d'avoir à recommencer
	format = request.POST.get('format')
	if format == "TEXT" :
		title = request.POST.get('Titre')
		content = request.POST.get('Texte')
		illustration = request.POST.get('Illustration')
		partageable = request.POST.get('Partageable')
		text_data = {'title': title, 'content': content, 'illustration': illustration, 'partageable': partageable}
		if PostTextForm(request.POST).is_valid() :
			new_post = Post(
				format='TEXT',
				title=title,
				content=content,
				illustration=illustration,
				shareable=(partageable==True),
				author=request.user,
				channel=Channel.objects.get(pk=1), # change when adding more channels
				)
			new_post.save()
			new_post_adress = "/p/" + new_post.slug
			rank_posts()
			logging.info(
				"New text link posted by {username} : {title}".format(
					username=request.user.username,
					title=request.POST.get('title')
					).encode('utf8')
				)
			messages.success(request, "Votre post est publié.")
			return HttpResponseRedirect(new_post_adress)
		else :
			messages.error(request, "Votre post n'a pas été publié : {}".format(PostTextForm(request.POST).errors), extra_tags='safe')

	return render(request, 'aggregateur/nouveau_post.html', {'post_text_form': PostTextForm(initial=text_data), 'post_link_form': PostLinkForm(initial=link_data), 'page_title': 'Nouveau post', })
