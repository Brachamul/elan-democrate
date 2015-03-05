from django.db import models

from django.contrib.auth.models import User

from fichiers_adherents.models import Adhérent

class Profil(models.Model):
	# Ce profil est rempli par l'utilisateur ou un administrateur lorsque le modèle officiel n'est pas à jour
	user = models.OneToOneField(User, primary_key=True)
	adherent = models.OneToOneField(Adhérent, blank=True, null=True)
	nom_courant = models.CharField(max_length=255, blank=True, null=True)
	notes = models.TextField(blank=True, null=True) # Visible uniquement par les responsables