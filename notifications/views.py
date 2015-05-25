import logging
from django.conf import settings
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.core.exceptions import ObjectDoesNotExist
from django.forms.models import model_to_dict
from django.http import HttpResponseRedirect, HttpResponse, HttpRequest, Http404, JsonResponse
from django.shortcuts import get_object_or_404, render, render_to_response, redirect

from .models import *

@login_required
def json(request, filter):
	"""	Réponse JSON contenant toutes les notifications """
	notifications = []
	for notification in Notification.objects.filter(destinataire=request.user) : # try reducing it with [:12]
		notification = convert_notification_to_html(notification)
		notifications.append(notification)
	return JsonResponse(notifications, safe=False)

def convert_notification_to_html(notification):
	acteur = notification.acteur
	if notification.type_acteur.name == "utilisateur" :
		acteur_utilisateur = User.objects.get(pk=notification.id_acteur)
		acteur = "<a href='/m/{pk}'>{nom_courant}</a>".format(pk=acteur_utilisateur.pk, nom_courant=acteur_utilisateur.profil.nom_courant).encode('utf-8')
	action = notification.action
	cible = notification.cible
	lieu = notification.lieu
	variables = { 'acteur': acteur, 'action': action, 'cible': cible, 'lieu': lieu }
	if notification.cible:
		if notification.lieu:
			return u'%(acteur)s %(action)s %(lieu)s sur %(cible)s' % variables
		return u'%(acteur)s %(action)s %(cible)s' % variables
	if notification.lieu:
		return u'%(acteur)s %(action)s %(lieu)s' % variables
	return u'%(acteur)s %(action)s' % variables

#	def get_actor(actor_object_id, actor_content_type):
#		if actor_content_type == 4 :
#			try : actor = User.objects.get(id=actor_object_id)
#			except User.DoesNotExist : return "Un compte supprimé"
#			else : return actor.profil.nom_courant
#		else : return None
#	
#	notification['actor'] = get_actor(notification['actor_object_id'], notification['actor_content_type'])
#	
