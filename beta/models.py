from datetime import datetime, timedelta

from django.contrib.auth.models import User
from django.core.exceptions import ObjectDoesNotExist
from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver

class BetaCandidat(models.Model):
	nom_courant = models.CharField(max_length=255, help_text="Prénom et Nom")
	email = models.EmailField(help_text="Idéalement celle que le MoDem a dans son fichier")
	departement = models.CharField(max_length=20, help_text="C'est le numéro de la fédé, par exemple '78'")
	fonctions = models.CharField(max_length=1024, help_text="Si vous êtes quelqu'un d'important", null=True, blank=True)
	telephone = models.CharField(max_length=20, null=True, blank=True)
	bio = models.TextField(max_length=255, help_text="Une courte présentation de vous-même, qui fera partie de votre profil", null=True, blank=True)