import logging
from django.core.exceptions import ObjectDoesNotExist
from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver

from django.contrib.auth.models import User
from fichiers_adherents.models import Adhérent

class Profil(models.Model):
	# Ce profil est rempli par l'utilisateur ou un administrateur lorsque le modèle officiel n'est pas à jour
	user = models.OneToOneField(User, blank=True, null=True)
	adherent = models.OneToOneField(Adhérent, blank=True, null=True)
	nom_courant = models.CharField(max_length=255, blank=True, null=True)
	bio = models.TextField(max_length=255, blank=True, null=True)
	notes = models.TextField(blank=True, null=True) # Visible uniquement par les responsables
	def __str__(self): return self.nom_courant

@receiver(post_save, sender=Adhérent) # Quand un adhérent est ajouté via le fichier, on créé un profil 
def generer_le_profil_d_un_adherent(sender, created, **kwargs):
	if created :
		adherent = kwargs.get('instance')
		try : user = User.objects.get(email=adherent.email) # a t-on déjà un utilisateur avec cette adresse mail ?
		except User.DoesNotExist : # si non, on peut créer le profil
			nouveau_profil = Profil(adherent=adherent, nom_courant=(adherent.prénom + " " + adherent.nom))
			nouveau_profil.save()
		else :
			logging.warning("Un nouvel adhérent a indiqué une adresse mail déjà présente dans la base de donnée, il faut peut-être fusionner le Membre avec l'Adhérent".encode('utf8'))
#		if user didn't have an adhérent, then merge them

@receiver(post_save, sender=User) # Quand un adhérent est ajouté via le fichier, on créé un profil 
def generer_le_profil_d_un_utilisateur(sender, created, **kwargs):
	if created :
		user = kwargs.get('instance')
		try : adherent = Adhérent.objects.get(email=user.email) # logiquement, l'utilisateur a été créé parce qu'il existait dans la base adhérent, et a été authentifié par email
		except Adhérent.DoesNotExist : # sinon, on lui créé un profil
			nouveau_profil = Profil(user=user)
			nouveau_profil.save()
			logging.warning("Un utilisateur a été créé sans avoir d'email reconnu dans la base adhérents".encode('utf8'))
		else : # mais s'il était déjà dans la base, on peut lier les comptes 
			ancien_profil = Profil.objects.get(adherent=adherent)
			ancien_profil.user = user
			ancien_profil.save(update_fields=['user'])