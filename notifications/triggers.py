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
from aggregateur.models import Comment, Post, Channel, WantToJoinChannel

from .views import Notification

def join_private_channel_allowed(request, channel, candidate):
	action = "Votre abonnement à la chaîne \"{}\" a été validé.".format(channel.name)
	nouvelle_notif = Notification( destinataire = candidate, action = action, cible = channel )

def join_private_channel_denied(request, channel, candidate):
	action = "Votre abonnement à la chaîne \"{}\" a été refusé.".format(channel.name)
	nouvelle_notif = Notification( destinataire = candidate, action = action, cible = channel )