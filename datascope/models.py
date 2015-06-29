from datetime import datetime, timedelta

from django.contrib.auth.models import User
from django.core.exceptions import ObjectDoesNotExist
from django.db import models
from django.dispatch import receiver

from membres.models import Profil
from fichiers_adherents.models import Adhérent

class VueFederation(models.Model):
	federation = models.CharField(max_length=255)
	def __str__(self): return self.federation
	def adherents(self): return Adhérent.objects.filter(fédération=self.federation)
	class Meta: permissions = (('gere_les_mandats', 'gère les mandats'),)

def mettre_a_jour_les_federations():
	federations = Adhérent.objects.all().values('fédération').distinct()
	for federation in federations :
		try : vue = VueFederation(federation=federation['fédération'])
		except VueFederation.DoesNotExist :
			nouvelle_vue = VueFederation(federation=federation['fédération'])
			nouvelle_vue.save()