import logging
from django.conf import settings
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.core import serializers
from django.core.exceptions import ObjectDoesNotExist
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.core.urlresolvers import reverse
from django.http import HttpResponseRedirect, HttpResponse, HttpRequest, Http404, JsonResponse
from django.shortcuts import get_object_or_404, render, render_to_response, redirect
from django.template import RequestContext
from django.views import generic
from django.views.generic import TemplateView, DetailView
from django.contrib.auth.models import User
from membres.models import Profil

from .models import *
from .forms import *


def ChatRoomFeed(request, channel_slug):
	channel = get_object_or_404(Channel, slug=channel_slug)
	messages = serializers.serialize("json", Message.objects.filter(channel=channel)[:100])
	return HttpResponse(messages, content_type="application/json")

def ChatRoomView(request, channel_slug):
	channel = get_object_or_404(Channel, slug=channel_slug)
	page_title = "Salle de discussion pour la chaîne {}".format(channel.name.capitalize())
	return render(request, 'chatrooms/chatroom.html', {
		'channel': channel,
		'page_title': page_title
		} )