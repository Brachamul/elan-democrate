from django.contrib import messages
from django.core.urlresolvers import reverse
from django.core.exceptions import ObjectDoesNotExist
from django.http import HttpResponseRedirect, HttpResponse, HttpRequest, Http404
from django.shortcuts import get_object_or_404, render, render_to_response, redirect
from django.template import RequestContext
from django.views import generic
from django.views.generic.base import TemplateView

from .models import *

### Card

def all(request):
	# temporary catch all url for posts
	HttpResponseRedirect('/')

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