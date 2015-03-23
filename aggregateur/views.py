from django.contrib import messages
from django.core.urlresolvers import reverse
from django.core.exceptions import ObjectDoesNotExist
from django.http import HttpResponseRedirect, HttpResponse, HttpRequest, Http404
from django.shortcuts import get_object_or_404, render, render_to_response, redirect
from django.template import RequestContext
from django.views import generic
from django.views.generic.base import TemplateView

from .models import *
from .forms import *

def all(request):
	# temporary catch all url for posts
	return HttpResponseRedirect('/')



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
			post.link = post.slug
			# except if post is a LINK !
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
		post_type = request.POST.get('post-type')
		if post_type == "text" :
			print("Un nouveau texte a été posté.")
			if PostTextForm(request.POST).is_valid() :
				print("Il est valide !")
			else :
				print("Il n'est pas valide ...")

		elif post_type == "link" :
			print("Un nouveau lien a été posté.")
			if PostLinkForm(request.POST).is_valid() :
				print("Il est valide !")
			else :
				print("Il n'est pas valide ...")
		else:
			messages.warning(request, "Bug dans la matrice !")

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