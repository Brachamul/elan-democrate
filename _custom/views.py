import logging
from django.conf import settings
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.core.exceptions import ObjectDoesNotExist
from django.forms.models import model_to_dict
from django.http import HttpResponseRedirect, HttpResponse, HttpRequest, Http404, JsonResponse
from django.shortcuts import get_object_or_404, render, render_to_response, redirect

@login_required
def custom_notifications(request):
	"""
	Réponse JSON contenant les notifications
	"""
	notifications = []
	for notification in request.user.notifications.all()[:2] :
		notification = model_to_dict(notification)
		notification['actor'] = get_actor(notification['actor_object_id'], notification['actor_content_type'])
		notifications.append(notification)
	return JsonResponse(notifications, safe=False)

def get_actor(actor_object_id, actor_content_type):
	if actor_content_type == 4 :
		try : actor = User.objects.get(id=actor_object_id)
		except User.DoesNotExist : return "Un compte supprimé"
		else : return actor.profil.nom_courant
	else : return None