from datetime import datetime, timedelta

from django.contrib.auth.models import User
from django.core.exceptions import ObjectDoesNotExist
from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver

from membres.models import Profil
from fichiers_adherents.models import Adhérent

class VueFederation(models.Model):
	federation = models.CharField(max_length=255, unique=True)
	def __str__(self): return self.federation
	def adherents(self): return Adhérent.objects.filter(fédération=self.federation)
	class Meta: permissions = (('gere_les_mandats', 'gère les mandats'),)

def mettre_a_jour_les_federations():
	federations = []
	federations_du_fichier = Adhérent.objects.all().values('fédération').annotate(n=models.Count('pk'))
	for federation in federations_du_fichier : federations.append(str(federation['fédération']))
	for federation in federations :
		print (federation)
		try : vue = VueFederation.objects.get(federation=federation)
		except VueFederation.DoesNotExist :
			nouvelle_vue = VueFederation(federation=federation)
			nouvelle_vue.save()
	return VueFederation.objects.all()


from mandats.models import Detenteur
@receiver(post_save, sender=Detenteur)
def accorder_une_vue_a_un_detenteur(sender, created, **kwargs):
	if created :
		detenteur = kwargs.get('detenteur')
		if detenteur.mandat.institution.code and detenteur.titre == "Président" or detenteur.titre == "Secrétaire" :
			if detenteur.mandat.institution.classe == "Fédération JDem" :
				try : vue = VueFederation(federation=detenteur.mandat.institution.code)
				except VueFederation.DoesNotExist : pass
				else :
					detenteur.peut_voir_la_federation.add(vue)
					detenteur.save()