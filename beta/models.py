from datetime import datetime, timedelta

from django.contrib.auth.models import User
from django.core.exceptions import ObjectDoesNotExist
from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver

class BetaCandidat(models.Model):
	nom_courant = models.CharField(max_length=255, verbose_name="Prénom et Nom")
	email = models.EmailField(help_text="Idéalement celle que le MoDem a dans son fichier")
	fonctions = models.CharField(max_length=1024, help_text="Si vous êtes quelqu'un d'important", null=True, blank=True)
	telephone = models.CharField(max_length=20, null=True, blank=True)
	def __str__(self) : return self.nom_courant + ', ' + self.fonctions