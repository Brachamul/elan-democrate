from django.conf import settings
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.core.exceptions import ObjectDoesNotExist
from django.core.urlresolvers import reverse
from django.forms.models import model_to_dict
from django.http import HttpResponseRedirect, HttpResponse, HttpRequest, Http404
from django.shortcuts import get_object_or_404, render, render_to_response, redirect

from .models import *

@login_required
def notifications(request):
	"""	Réponse data contenant des notifications selon un filtre """
	notifications = []
	for notification in Notification.objects.filter(destinataire=request.user) : # try reducing it with [:12]
		notification = check_if_is_system_notification(request, notification)
		if not notification.is_system :
			notification.fulltext = notification_fulltext(request, notification)
			url = notification_url(notification)
			if url : notification.url = url
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

	action = notification.action

	acteur = notification.acteur
	if acteur:
		type_acteur = notification.type_acteur.name
		if type_acteur == "utilisateur" :
			acteur = User.objects.get(pk=notification.id_acteur).profil.nom_courant

	cible = notification.cible
	if cible :
		type_cible = notification.type_cible.name
		if type_cible == "post" :
			if cible.author == request.user : cible = ('à votre post "{titre_du_post}"'.format(titre_du_post=cible))
			else : cible = ('au post "{titre_du_post}"'.format(titre_du_post=cible))
		if type_cible == "comment" :
			if cible.author == request.user : cible = ('à votre commentaire')
			else : cible = ('à un commentaire')

	lieu = notification.lieu
	if lieu :
		type_lieu = notification.type_lieu.name
		if type_lieu == "post" :
			if lieu.author == request.user : lieu = ('sur votre post "{titre_du_post}"'.format(titre_du_post=lieu))
			else : lieu = ('sur le post "{titre_du_post}"'.format(titre_du_post=lieu))

	variables = { 'acteur': acteur, 'action': action, 'cible': cible, 'lieu': lieu }
	if cible and lieu : return '%(acteur)s %(action)s %(cible)s %(lieu)s.' % variables
	elif cible : return '%(acteur)s %(action)s %(cible)s.' % variables
	elif lieu : return '%(acteur)s %(action)s %(lieu)s.' % variables
	elif acteur : return '%(acteur)s %(action)s.' % variables
	else : return '%(action)s.' % variables # S'il n'y a qu'une action, c'est un message système


def notification_url(notification):
	cible = notification.cible
	if cible :
		if notification.type_cible.name == "post" : return reverse('post', args=(cible.date.year, cible.slug,))
		if notification.type_cible.name == "comment" : return reverse('commentaire', args=(cible.post_racine().slug, cible.pk,))
		if notification.type_cible.name == "channel" : return reverse('chaine', kwargs={ 'channel_slug': cible.slug })
		if notification.type_cible.name == "want_to_join_channel" : return reverse ('wanttojoin_channel', args=(cible.channel.slug))
	else : return False

def check_if_is_system_notification(request, notification):
	notification.is_system = False # by default, it's not a system notification, let's check if it is
	if notification.action == "welcome-notification" :
		notification.is_system = True
		notification.fulltext = 'Bienvenue sur Élan Démocrate ! Pour commencer, cliquez ici pour renseigner votre profil !'
		notification.url = reverse('profil', kwargs={ 'pk': request.user.pk })
	if notification.action == "dummy-notification" :
		notification.is_system = True
		notification.fulltext = 'Ceci est une notification test !'
		notification.url = '/'
	if notification.is_system : notification.icon = "cogs"
	return notification

def notifyme(request):
	'''Dummy notification used for testing purposes'''
	Notification.objects.create( destinataire = request.user, action = "dummy-notification" )
	return HttpResponseRedirect('/')