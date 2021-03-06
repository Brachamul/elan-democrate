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
	notification_events = NotificationEvent.objects.filter(recipient=request.user)
	if notification_events :
		notifications = []
		for notification in notification_events  : # try reducing it with [:12]
#			notification = check_if_is_system_notification(request, notification)
#			if not notification.is_system :
			
			notification.fulltext = notification_fulltext(request, notification)
#				url = notification_url(notification)
#				if url : notification.url = url
			notifications.append(notification)
	else : notifications = False
	return render(request, 'notifications/notifications.html', {'notifications': notifications})

def number_of_unseen_notifications(request):
	"""	Counts the number of unseen notifications """
	return HttpResponse(NotificationEvent.objects.filter(recipient=request.user, seen=False).count())

def mark_all_notifications_as_seen(request):
	"""	Marks all of the user's notifications as seen """
	unseen_notifications = NotificationEvent.objects.filter(recipient=request.user, seen=False)
	for notification in unseen_notifications :
		notification.seen = True
		notification.save()
	return HttpResponse()

def notification_fulltext(request, notification):

	if notification.category == "OLD" : return "This is a legacy notification"
	if notification.category == "TEST" : return "This is a test notification"
	return "Le texte de cette notification n'a pas pu être généré."

#	action = notification.action
#
#	acteur = notification.acteur
#	if acteur:
#		type_acteur = notification.type_acteur.name
#		if type_acteur == "utilisateur" :
#			acteur = User.objects.get(pk=notification.id_acteur).profil.nom_courant
#
#	cible = notification.cible
#	if cible :
#		type_cible = notification.type_cible.name
#		if type_cible == "post" :
#			if cible.author == request.user : cible = 'à votre post "{titre_du_post}"'.format(titre_du_post=cible)
#			else : cible = 'au post "{titre_du_post}"'.format(titre_du_post=cible)
#		if type_cible == "comment" :
#			if cible.author == request.user : cible = 'à votre commentaire'
#			else : cible = 'à un commentaire'
#		if type_cible == "channel" :
#			if request.user in cible.moderators.all() : cible = 'votre chaîne \"{}\"'.format(cible.name)
#			else : cible = 'la chaîne \"{}\"'.format(cible.name)
#			
#
#	lieu = notification.lieu
#	if lieu :
#		type_lieu = notification.type_lieu.name
#		if type_lieu == "post" :
#			if lieu.author == request.user : lieu = ('sur votre post "{titre_du_post}"'.format(titre_du_post=lieu))
#			else : lieu = ('sur le post "{titre_du_post}"'.format(titre_du_post=lieu))
#
#	variables = { 'acteur': acteur, 'action': action, 'cible': cible, 'lieu': lieu }
#	if cible and lieu : return '%(acteur)s %(action)s %(cible)s %(lieu)s.' % variables
#	elif cible : return '%(acteur)s %(action)s %(cible)s.' % variables
#	elif lieu : return '%(acteur)s %(action)s %(lieu)s.' % variables
#	elif acteur : return '%(acteur)s %(action)s.' % variables
#	else : return '%(action)s.' % variables # S'il n'y a qu'une action, c'est un message système

def notifyme(request):
	'''Dummy notification used for testing purposes'''
	NotificationEvent.objects.create( recipient = request.user, category = "TEST")
	return HttpResponseRedirect('/')

def notification_url(notification):
	cible = notification.cible
	if cible :
		if notification.type_cible.name == "post" : return reverse('post', args=(cible.date.year, cible.slug,))
		if notification.type_cible.name == "comment" : return reverse('commentaire', kwargs={ 'year': cible.post_racine().date.year, 'slug': cible.post_racine().slug, 'pk': cible.pk })
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
	if notification.action == "new-beta-signup" :
		notification.is_system = True
		notification.fulltext = "Quelqu'un s'est inscrit à la beta !"
		notification.url = '/beta/list'
	if notification.is_system : notification.icon = "cogs"
	return notification

