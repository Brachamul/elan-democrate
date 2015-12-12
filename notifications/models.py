import logging
import uuid
from django.core.exceptions import ObjectDoesNotExist
from django.core.urlresolvers import reverse
from django.conf import settings
from django.contrib.contenttypes.models import ContentType
from django.contrib.contenttypes.fields import GenericForeignKey
from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.utils.timesince import timesince
from django.contrib.auth.models import User
from fichiers_adherents.models import Adherent

class NotificationEventCategory:
	def __init__(self, name, description):
		self.name = name
		self.description = description
#		self.choice = (name, description) # A tuple used for category choices in the NotificationEvent model


settings.NOTIFICATION_EVENTS += (
	NotificationEventCategory(name="WELCOME", description="A new user has joined"),
	NotificationEventCategory(name="OLD", description="A legacy notification"),
	NotificationEventCategory(name="TEST", description="A test notification"),
 	)

def NotificationEventsCategoryChoices(events=settings.NOTIFICATION_EVENTS):
	choices = []
	for event in events :
		choices += (event.name, event.description),
	return choices

class NotificationEvent(models.Model):

	''' Notification events are usually triggered by user actions and kept as a log of what has happened '''

	id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)

	category = models.CharField(max_length=255, choices=NotificationEventsCategoryChoices(), default='OLD')

	# Recipient
	recipient = models.ForeignKey(User)
	seen = models.BooleanField(default=False) # vue implique que l'utilisateur l'a simplement affichée
	read = models.BooleanField(default=False) # lue implique que l'utilisateur ait cliqué dessus
	emailed = models.BooleanField(default=False)

	# Sender
	sender_id = models.CharField(max_length=255, blank=True, null=True) # Check it's not sending to self
	sender_type = models.ForeignKey(ContentType, related_name='notification_sender', blank=True, null=True)
	sender = GenericForeignKey('sender_type', 'sender_id')

	# Target
	target_id = models.CharField(max_length=255, blank=True, null=True) # Check it's not sending to self
	target_type = models.ForeignKey(ContentType, related_name='notification_target', blank=True, null=True)
	target = GenericForeignKey('target_type', 'target_id')

	# Accessory
	accessory_id = models.CharField(max_length=255, blank=True, null=True) # Check it's not sending to self
	accessory_type = models.ForeignKey(ContentType, related_name='notification_accessory', blank=True, null=True)
	accessory = GenericForeignKey('accessory_type', 'accessory_id')

	# Date
	date = models.DateTimeField(auto_now_add=True)

	class Meta:
		ordering = ('-date', )

	def __str__(self):
		"[{date}] {category} - From {actor} to {sender} through {accessory}".format(
			self.date, self.category, self.actor, self.sender, self.accessory)

	def marquer_lu(self):
		if self.non_lu:
			self.non_lu = False
			self.save()

from django.contrib import admin
admin.site.register(NotificationEvent)

### Signals
from aggregateur.models import Comment, Post, Channel, WantToJoinChannel

@receiver(post_save, sender=Comment)
def notifier_lauteur_du_parent(sender, created, **kwargs):
	if created :
		commentaire = kwargs.get('instance')
		if commentaire.parent_post :
			nouvelle_notif = NotificationEvent(
				category = "NEW_REPLY_TO_POST",
				receiver = commentaire.parent_post.author,
				sender = commentaire.author,
				target = commentaire.parent_post,
				)
		else :
			nouvelle_notif = NotificationEvent(
				category = "NEW_REPLY_TO_COMMENT",
				receiver = commentaire.parent_comment.author,
				sender = commentaire.author,
				target = commentaire.parent_comment,
				accessory = commentaire.post_racine(),
				)
		if nouvelle_notif.receiver != nouvelle_notif.sender : # On ne notifie pas celui qui a généré la notif !
			nouvelle_notif.save()

@receiver(post_save, sender=User)
def notification_apres_creation_de_compte(sender, created, **kwargs):
	if created :
		user = kwargs.get('instance')
		nouvelle_notif = NotificationEvent(category="WELCOME", receiver=user)
		nouvelle_notif.save()

@receiver(post_save, sender=WantToJoinChannel)
def want_to_join_channel_notification(sender, created, **kwargs):
	if created :
		joining_instance = kwargs.get('instance')
		user = joining_instance.user
		channel = joining_instance.channel
		for moderator in channel.moderators.all() :
			nouvelle_notif = NotificationEvent(
				category = 'CHANNEL_JOIN_REQUEST',
				receiver = moderator,
				sender = user,
				target = channel,
				)
		nouvelle_notif.save()