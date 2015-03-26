from django.contrib import messages
from django.core.urlresolvers import reverse
from django.core.exceptions import ObjectDoesNotExist
from django.http import HttpResponseRedirect, HttpResponse, HttpRequest, Http404
from django.shortcuts import get_object_or_404, render, render_to_response, redirect
from django.template import RequestContext
from django.views import generic
from django.views.generic import TemplateView, DetailView

from .models import *
from .forms import *

def all(request):
	# temporary catch all url for posts
	return HttpResponseRedirect('/')

class afficher_le_post(DetailView):

	model = Post
	template_name = "aggregateur/afficher_le_post.html"

	def get_context_data(self, **kwargs):
		context = super(DetailView, self).get_context_data(**kwargs)
		context['post'] = get_object_or_404(Post, slug=self.kwargs['slug'])
		return context

### Card

def aggregateur(request, fil):
	try :
		print ("trying posts")
		posts = Post.objects.all().order_by('-score')[:20]
	#
	except Post.DoesNotExist :
		print ("post does not exist")
		return False
	else :
		for post in posts :
			if post.format == "LINK" : post.link = post.content
			else : post.link = post.slug
		print ("ok, post exists")
		return { 'posts': posts, 'template': "aggregateur/carte_aggregateur.html", }

def scorify():
	for post in Post.objects.all() :
		pos = Vote.objects.filter(post=post, color="POS").count()
		neg = Vote.objects.filter(post=post, color="NEG").count()
		post.score = pos-neg
		post.save()

def nouveau_post(request):
	if request.method == "POST":
		format = request.POST.get('format')
		if format == "TEXT" :
			print("Un nouveau texte a été posté.")
			if PostTextForm(request.POST).is_valid() :
				print("Il est valide !")
				new_post = Post(
					format='TEXT',
					title=request.POST.get('title'),
					content=request.POST.get('content'),
					author=request.user,
					channel=Channel.objects.get(pk=1), # change when adding more channels
				#	illustration=
					)
				new_post.save()
				new_post_adress = "/p/" + new_post.slug
				messages.success(request, "Votre post est publié.")
				print ("Nouveau texte à l'adresse" + new_post_adress)
				return HttpResponseRedirect(new_post_adress)
			else :
				print("Il n'est pas valide ...")

		elif format == "LINK" :
			print("Un nouveau lien a été posté.")
			if PostLinkForm(request.POST).is_valid() :
				print("Il est valide !")
				new_post = Post(
					format = 'LINK',
					title=request.POST.get('title'),
					content=request.POST.get('url'),
					author=request.user,
					channel=Channel.objects.get(pk=1), # change when adding more channels
				#	illustration=
					)
				new_post.save()
				new_post_adress = "/p/" + new_post.slug
				messages.success(request, "Votre post est publié.")
				print ("Nouveau lien à l'adresse" + new_post_adress)
				return HttpResponseRedirect(new_post_adress)
			else :
				print("Il n'est pas valide ...")
		else:
			messages.warning(request, "Il y a un bug dans la matrice !")

#		 upload_form.is_valid():
#			messages.success(request, "Ce post aurait été valide, mais la fonction de postage n'a pas encore été activée.")
		# 	return render(request, 'aggregateur/nouveau_post.html', {
		#		'fichier': nouveau_fichier,
		#		'nombre_nouveaux_adherents': nombre_nouveaux_adherents,
		#		'nombre_réadhésions': nombre_réadhésions,
		#			})
			
#		else :
#			messages.error(request, "Ce post ne semble pas valide.")			
		return HttpResponseRedirect('')
	else :
		return render(request, 'aggregateur/nouveau_post.html', {'post_text_form': PostTextForm(), 'post_link_form': PostLinkForm(), })