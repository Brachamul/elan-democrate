from django.db import models

from django.contrib.auth.models import User

class MetaInstitution(models.Model):
	nom = models.CharField(max_length=255) # Commune, Fédération, ...
	def __str__(self): return self.nom

class Institution(models.Model):
	nom = models.CharField(max_length=1023) # Jeunes Démocrates, Paris
	prefixe = models.CharField(max_length=10) # "des" Jeunes Démocrates, "de" Paris
	classe = models.ForeignKey(MetaInstitution, blank=True, null=True) # Commune, Fédération, ...
	def __str__(self): return self.nom

class Mandat(models.Model):
	institution = models.ForeignKey(Institution) 
	date_de_debut = models.DateField()
	date_de_fin = models.DateField(blank=True, null=True)
	def __str__(self): return "{institution} {annee}".format(institution=self.institution, annee=self.date_de_debut.year)

class Detenteur(models.Model):
	user = models.OneToOneField(User, primary_key=True)
	mandat = models.OneToOneField(Mandat)
	titre = models.CharField(max_length=1023) # Membre du Bureau, Vice-Président, Conseiller Municipal, ...
	charge = models.CharField(max_length=1023, blank=True, null=True) # en charge de la communication, délégué aux espaces verts, ...
	date_de_debut = models.DateField(blank=True, null=True) # en cas de début différent du mandat
	date_de_fin = models.DateField(blank=True, null=True) # en cas de fin différente du mandat
	def __str__(self): return "{user}, {titre} {prefixe} {institution}".format(user=self.user.profil.nom_courant, titre=self.titre, prefixe=self.mandat.institution.prefixe, institution=self.mandat.institution.nom)