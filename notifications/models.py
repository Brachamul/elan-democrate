import logging
from django.core.exceptions import ObjectDoesNotExist
from django.core.urlresolvers import reverse
from django.contrib.contenttypes.models import ContentType
from django.contrib.contenttypes.fields import GenericForeignKey
from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.utils.timesince import timesince
from django.contrib.auth.models import User
from fichiers_adherents.models import Adherent

class NotificationEvent(models.Model):

	# Destinataire
	destinataire = models.ForeignKey(User, related_name='destinataire_de_la_notif')
	lue = models.BooleanField(default=False) # lue implique que l'utilisateur ait cliqué dessus
	vue = models.BooleanField(default=False) # vue implique que l'utilisateur l'a simplement affichée
	prevenu_par_email = models.BooleanField(default=False)

	# Acteur
	id_acteur = models.CharField(max_length=255, blank=True, null=True) # Check it's not sending to self
	type_acteur = models.ForeignKey(ContentType, related_name='acteur_de_la_notif', blank=True, null=True)
	acteur = GenericForeignKey('type_acteur', 'id_acteur')

	# Action
	action = models.CharField(max_length=255)
#	is_system = models.BooleanField(default=False)
	
	# Cible
	id_cible = models.CharField(max_length=255, blank=True, null=True)
	type_cible = models.ForeignKey(ContentType, related_name='cible_de_la_notif', blank=True, null=True)
	cible = GenericForeignKey('type_cible', 'id_cible')

	# Lieu
	id_lieu = models.CharField(max_length=255, blank=True, null=True)
	type_lieu = models.ForeignKey(ContentType, related_name='lieu_de_la_notif', blank=True, null=True)
	lieu = GenericForeignKey('type_lieu', 'id_lieu')

	# Date
	date = models.DateTimeField(auto_now_add=True)

	class Meta:
		ordering = ('-date', )

	def __str__(self):
		variables = {
			'acteur': self.acteur,
			'action': self.action,
			'cible': self.cible,
			'lieu': self.lieu,
			'destinataire': self.destinataire.profil,
		}
		if self.cible:
			if self.lieu:
				return u'%(acteur)s %(action)s %(lieu)s sur %(cible)s' % variables
			return u'%(acteur)s %(action)s %(cible)s' % variables
		if self.lieu:
			return u'%(acteur)s %(action)s %(lieu)s' % variables
		if self.acteur:
			return u'%(acteur)s %(action)s' % variables
		return u'%(action)s pour %(destinataire)s' % variables

	def marquer_lu(self):
		if self.non_lu:
			self.non_lu = False
			self.save()

from django.contrib import admin
admin.site.register(Notification)

### Signals
from aggregateur.models import Comment, Post, Channel, WantToJoinChannel

@receiver(post_save, sender=Comment)
def notifier_lauteur_du_parent(sender, created, **kwargs):
	if created :
		commentaire = kwargs.get('instance')
		if commentaire.parent_post :
			nouvelle_notif = Notification(
				destinataire = commentaire.parent_post.author,
				acteur = commentaire.author,
				action = "a répondu",
				cible = commentaire.parent_post,
				)
		else :
			nouvelle_notif = Notification(
				destinataire = commentaire.parent_comment.author,
				acteur = commentaire.author,
				action = "a répondu",
				cible = commentaire.parent_comment,
				lieu = commentaire.post_racine(),
				)
		if nouvelle_notif.destinataire != nouvelle_notif.acteur : # On ne notifie pas celui qui a généré la notif !
			nouvelle_notif.save()

@receiver(post_save, sender=User)
def notification_apres_creation_de_compte(sender, created, **kwargs):
	if created :
		user = kwargs.get('instance')
		nouvelle_notif = Notification(
			destinataire = user,
			action = "welcome-notification"
			)
		nouvelle_notif.save()

@receiver(post_save, sender=WantToJoinChannel)
def want_to_join_channel_notification(sender, created, **kwargs):
	if created :
		joining_instance = kwargs.get('instance')
		user = joining_instance.user
		channel = joining_instance.channel
		action = 'a demandé à rejoindre'
		for moderator in channel.moderators.all() :
			nouvelle_notif = Notification(
				destinataire = moderator,
				acteur = user,
				action = action,
				cible = channel,
				)
		nouvelle_notif.save()