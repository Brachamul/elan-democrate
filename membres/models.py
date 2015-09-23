import logging
from django.core.exceptions import ObjectDoesNotExist
from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver

from django.contrib.auth.models import User
from fichiers_adherents.models import Adherent


class Profil(models.Model):
	# Ce profil est rempli par l'utilisateur ou un administrateur lorsque le modèle officiel n'est pas à jour
	user = models.OneToOneField(User, blank=True, null=True)
	adherent = models.OneToOneField(Adherent, blank=True, null=True, on_delete=models.SET_NULL)
	nom_courant = models.CharField(default="Anonyme", max_length=255)
	bio = models.TextField(max_length=255, blank=True, null=True)
	twitter = models.CharField(max_length=255, blank=True, null=True, help_text='Sans le @')
	notes = models.TextField(blank=True, null=True) # Visible uniquement par les responsables
	def email(self):
		email = None
		try : email = self.adherent.email
		except AttributeError : pass
		try : email = self.user.email
		except AttributeError : pass
		return email
	def __str__(self): return ("%s (%s)" % (self.nom_courant, self.email()))

@receiver(post_save, sender=Adherent) # Quand un adhérent est ajouté via le fichier, on créé un profil 
def generer_le_profil_d_un_adherent(sender, created, **kwargs):
	if created :
		adherent = kwargs.get('instance')
		try : user = User.objects.get(email=adherent.email) # a t-on déjà un utilisateur avec cette adresse mail ?
		except User.DoesNotExist : Profil.objects.create(adherent=adherent, nom_courant=adherent.nom_courant()) # si non, on peut créer le profil
		else : logging.warning("Un nouvel adhérent a indiqué une adresse mail déjà présente dans la base de donnée, il faut peut-être fusionner le Membre avec l'Adherent".encode('utf8'))
#		if user didn't have an adhérent, then merge them

@receiver(post_save, sender=User) # Quand un adhérent est ajouté via le fichier, on créé un profil 
def generer_le_profil_d_un_utilisateur(sender, created, **kwargs):
	if created :
		user = kwargs.get('instance')
		try : adherent = Adherent.objects.get(email=user.email) # logiquement, l'utilisateur a été créé parce qu'il existait dans la base adhérent, et a été authentifié par email
		except Adherent.DoesNotExist : # sinon, on lui créé un profil
			nouveau_profil = Profil(user=user)
			nouveau_profil.save()
			logging.warning("A user was created without an email in the adherent base.".encode('utf8'))
		else : # mais s'il était déjà dans la base, on peut lier les comptes 
			ancien_profil = Profil.objects.get(adherent=adherent)
			ancien_profil.user = user
			ancien_profil.save(update_fields=['user'])