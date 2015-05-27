import logging
from django.core.exceptions import ObjectDoesNotExist
from django.contrib.contenttypes.models import ContentType
from django.contrib.contenttypes.fields import GenericForeignKey
from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.utils.timesince import timesince
from django.contrib.auth.models import User
from fichiers_adherents.models import Adhérent

class Notification(models.Model):

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
		}
		if self.cible:
			if self.lieu:
				return u'%(acteur)s %(action)s %(lieu)s sur %(cible)s' % variables
			return u'%(acteur)s %(action)s %(cible)s' % variables
		if self.lieu:
			return u'%(acteur)s %(action)s %(lieu)s' % variables
		return u'%(acteur)s %(action)s' % variables

	def marquer_lu(self):
		if self.non_lu:
			self.non_lu = False
			self.save()

from django.contrib import admin
admin.site.register(Notification)

### Signals
from aggregateur.models import Comment, Post

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
		nouvelle_notif.save()