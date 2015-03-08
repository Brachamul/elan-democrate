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



def aggregateur(request, fil):
	try :
		print ("trying posts")
		posts = Post.objects.all()[:20]
	#.order_by('-date')
	#
	except Post.DoesNotExist :
		print ("post does not exist")
		return False
	else :
		print ("ok, post exists")
		return { 'posts': posts, 'template': "aggregateur/carte_aggregateur.html", }