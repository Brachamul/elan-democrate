import logging
from django.conf import settings
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.core.exceptions import ObjectDoesNotExist
from django.core.urlresolvers import reverse
from django.forms.models import model_to_dict
from django.http import HttpResponseRedirect, HttpResponse, HttpRequest, Http404, JsonResponse
from django.shortcuts import get_object_or_404, render, render_to_response, redirect

from .models import *

@login_required
def notifications(request):
	"""	Réponse data contenant des notifications selon un filtre """
	notifications = []
	for notification in Notification.objects.filter(destinataire=request.user) : # try reducing it with [:12]
		notification.fulltext = notification_fulltext(request, notification)
		notification.url = notification_url(notification)
		notifications.append(notification)
	return render(request, 'notifications/notifications.html', {'notifications': notifications})

def non_vues(request):
	"""	Réponse data donnant le nombre de notification non vues """
	return HttpResponse(Notification.objects.filter(destinataire=request.user, vue=False).count())

def marquer_vues(request):
	"""	Marque toutes les notifications de l'utilisateur comme étant vues """
	notifications_non_vues = Notification.objects.filter(destinataire=request.user, vue=False)
	for notification in notifications_non_vues :
		notification.vue = True
		notification.save()
	return HttpResponse()

def notification_fulltext(request, notification):

	acteur = notification.acteur
	if notification.type_acteur.name == "utilisateur" : acteur = User.objects.get(pk=notification.id_acteur).profil.nom_courant

	action = notification.action

	cible = notification.cible
	if cible :
		if notification.type_cible.name == "post" :
			if cible.author == request.user : cible = ('à votre post "{titre_du_post}"'.format(titre_du_post=cible))
			else : cible = ('au post "{titre_du_post}"'.format(titre_du_post=cible))
		if notification.type_cible.name == "comment" :
			if cible.author == request.user : cible = ('à votre commentaire')
			else : cible = ('à un commentaire')

	lieu = notification.lieu
	if lieu :
		if notification.type_lieu.name == "post" :
			if lieu.author == request.user : lieu = ('sur votre post "{titre_du_post}"'.format(titre_du_post=lieu))
			else : lieu = ('sur le post "{titre_du_post}"'.format(titre_du_post=lieu))

	variables = { 'acteur': acteur, 'action': action, 'cible': cible, 'lieu': lieu }
	if cible and lieu : return '%(acteur)s %(action)s %(cible)s %(lieu)s' % variables
	elif cible : return '%(acteur)s %(action)s %(cible)s' % variables
	elif lieu : return '%(acteur)s %(action)s %(lieu)s' % variables
	else : return '%(acteur)s %(action)s' % variables


def notification_url(notification):
	cible = notification.cible
	if cible :
		if notification.type_cible.name == "post" : return reverse('post', args=(cible.slug,))
		if notification.type_cible.name == "comment" : return reverse('commentaire', args=(cible.post_racine().slug, cible.pk,))