from datetime import datetime, timedelta

from django.contrib.auth.models import User
from django.core.exceptions import ObjectDoesNotExist
from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver

from membres.models import Profil
from mandats.models import *
from fichiers_adherents.models import Adhérent

class VueFederation(models.Model):
	numero_de_federation = models.CharField(max_length=255, help_text="C'est le numéro de la fédé, par exemple '78'.")
	federation = models.ForeignKey(Institution)
	titres = models.ManyToManyField(Titre, help_text="Ce sont les titres qui permettent d'accéder aux données, par exemple 'secrétaire' et 'président'.")
	def __str__(self): return self.numero_de_federation
	def adherents(self): return Adhérent.objects.filter(fédération=self.numero_de_federation)
	def generer_les_titres_par_defaut(self):
		for titre in self.federation.institution.meta_institution.titres_par_defaut :
			self.titres.add(Titre.objects.get(pk=titre.pk))
			self.titres.save()
	class Meta: permissions = (('gere_les_mandats', 'gère les mandats'),)

def mettre_a_jour_les_federations():
	numeros_de_federations = []
	federations_du_fichier = Adhérent.objects.all().values('fédération').annotate(n=models.Count('pk'))
	for federation in federations_du_fichier : numeros_de_federations.append(str(federation['fédération']))
	for numero_de_federation in numeros_de_federations :
		try : vue = VueFederation.objects.get(numero_de_federation=numero_de_federation)
		except VueFederation.DoesNotExist :
			nouvelle_vue = VueFederation(numero_de_federation=numero_de_federation)
			nouvelle_institution = Institution.objects.get_or_create(nom=numero_de_federation, prefixe="du", meta_institution=MetaInstitution.objects.get(nom="Fédération JDem"))[0]
			nouvelle_vue.federation = nouvelle_institution
			nouvelle_vue.save()
	return VueFederation.objects.all()



@receiver(post_save, sender=Detenteur)
def accorder_une_vue_a_un_detenteur(sender, created, **kwargs):
#	if created :
#		detenteur = kwargs.get('instance')
#		if detenteur.mandat.institution.code and detenteur.titre.nom == "Président(e)" or detenteur.titre.nom == "Secrétaire" :
#			if detenteur.mandat.institution.classe == "Fédération JDem" :
#				try : vue = VueFederation(federation=detenteur.mandat.institution.code)
#				except VueFederation.DoesNotExist : pass
#				else :
#					detenteur.peut_voir_la_federation.add(vue)
#					detenteur.save()
	pass

