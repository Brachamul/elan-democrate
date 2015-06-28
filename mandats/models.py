from datetime import datetime, timedelta
from django.db import models
from django.contrib.auth.models import User
from membres.models import Profil

class MetaInstitution(models.Model):
	nom = models.CharField(max_length=255) # Commune, Fédération, ...
	def __str__(self): return self.nom
	class Meta: permissions = (('gere_les_mandats', 'gère les mandats'),)

class Institution(models.Model):
	nom = models.CharField(max_length=1023) # Jeunes Démocrates, Paris
	prefixe = models.CharField(max_length=10) # "des" Jeunes Démocrates, "de" Paris
	classe = models.ForeignKey(MetaInstitution, blank=True, null=True) # Commune, Fédération, ...
	def __str__(self): return self.nom
	class Meta: permissions = (('gere_les_mandats', 'gère les mandats'),)

class Mandat(models.Model):
	institution = models.ForeignKey(Institution) 
	date_de_debut = models.DateField(null=True)
	date_de_fin = models.DateField(blank=True, null=True)
	def __str__(self): return "{institution} {annee}".format(institution=self.institution, annee=self.date_de_debut.year)
	def actif(self):
		if self.date_de_fin : return datetime.now().date() < self.date_de_fin # Vrai si la date de fin n'est pas encore passée
		else : return True # Vrai également s'il n'y a pas de date de fin
	class Meta: permissions = (('gere_les_mandats', 'gère les mandats'),)

class Titre(models.Model):
	nom = models.CharField(max_length=1023) # Membre du Bureau, Vice-Président, Conseiller Municipal, ...
	def __str__(self): return self.nom
	class Meta: permissions = (('gere_les_mandats', 'gère les mandats'),)

class Detenteur(models.Model):
	profil = models.ForeignKey(Profil)
	mandat = models.ForeignKey(Mandat)
	titre = models.ForeignKey(Titre)
	charge = models.CharField(max_length=1023, blank=True, null=True) # en charge de la communication, délégué aux espaces verts, ...
	date_de_debut = models.DateField(blank=True, null=True) # en cas de début différent du mandat
	date_de_fin = models.DateField(blank=True, null=True) # en cas de fin différente du mandat
	def __str__(self): return "{titre} {prefixe} {institution}".format(titre=self.titre, prefixe=self.mandat.institution.prefixe, institution=self.mandat.institution.nom)
	def actif(self):
		if self.date_de_fin : return datetime.now().date() < self.date_de_fin # Vrai si la date de fin n'est pas encore passée
		else : return True # Vrai également s'il n'y a pas de date de fin
	class Meta: permissions = (('gere_les_mandats', 'gère les mandats'),)