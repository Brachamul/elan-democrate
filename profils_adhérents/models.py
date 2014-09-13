from django.db import models

from django.contrib.auth.models import User


class Profil(models.Model):
    # Ce profil est rempli par l'utilisateur ou un administrateur lorsque le modèle officiel n'est pas à jour
    user = models.OneToOneField(User)
    nom = models.CharField(max_length=255, blank=True)
    prénom = models.CharField(max_length=255, blank=True)
    ville = models.CharField(max_length=255, blank=True)
    pays = models.CharField(max_length=255, blank=True)
    tel = models.CharField(max_length=20, blank=True)
    email = models.CharField(max_length=255, blank=True)
    notes = models.TextField(blank=True) # Visible uniquement par les responsables