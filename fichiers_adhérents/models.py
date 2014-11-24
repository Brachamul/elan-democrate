from django.db import models

import os
from django.utils.text import slugify

from django.contrib.auth.models import User


class FichierAdhérents(models.Model):

	importé_à_date = models.DateTimeField(auto_now_add=True)
	importateur = models.ForeignKey(User)
	slug = models.SlugField(max_length=255)
	fichier_csv = models.FileField(upload_to='fichiers_adherents/')

	nombre_nouveaux_adherents = models.PositiveSmallIntegerField(null=True, blank=True, default=0)
	nombre_réadhésions = models.PositiveSmallIntegerField(null=True, blank=True, default=0)

	def __str__(self):
		return self.slug

	class Meta:
		verbose_name_plural = 'fichiers adhérents'
		permissions = (('peut_televerser', 'peut téléverser'),)


class Adhérent(models.Model):
	# Ce profil reprend une partie des données du fichier adhérent officiel du MoDem. Il ne peut pas être modifié par l'utilisateur
	num_adhérent = models.IntegerField(primary_key=True)
	user = models.OneToOneField(User, null=True) # lie chaque adhérent à un utilisateur
	fédération = models.IntegerField()
	date_première_adhésion = models.DateField()
	date_dernière_cotisation = models.DateField()
	genre = models.CharField(max_length=255, blank=True)
	nom = models.CharField(max_length=255)
	prénom = models.CharField(max_length=255)
	adresse_1 = models.CharField(max_length=255, blank=True)
	adresse_2 = models.CharField(max_length=255, blank=True)
	adresse_3 = models.CharField(max_length=255, blank=True)
	adresse_4 = models.CharField(max_length=255, blank=True)
	code_postal = models.IntegerField(blank=True)
	ville = models.CharField(max_length=255, blank=True)
	pays = models.CharField(max_length=255, blank=True)
	date_de_naissance = models.DateField()
	profession = models.CharField(max_length=255, blank=True)
	tel_portable = models.CharField(max_length=255, blank=True)
	tel_bureau = models.CharField(max_length=255, blank=True)
	tel_domicile = models.CharField(max_length=255, blank=True)
	email = models.CharField(max_length=255, blank=True)
	mandats = models.CharField(max_length=255, blank=True)
	commune = models.CharField(max_length=255, blank=True) # Dans le cas où la personne est élu dans une autre commune que sa ville de résidence.
	importé_par_le_fichier = models.ForeignKey(FichierAdhérents)

	def __str__(self):
		return '{} {}'.format(self.nom, self.prénom)


class AdhérentDuFichier(models.Model):

	class Meta:
		verbose_name_plural = "adhérents du fichier"

	fichier = models.ForeignKey(FichierAdhérents)
	adhérent = models.ForeignKey(Adhérent, null=True)
	fédération = models.IntegerField()
	date_première_adhésion = models.DateField()
	date_dernière_cotisation = models.DateField()
	num_adhérent = models.IntegerField()
	genre = models.CharField(max_length=255)
	nom = models.CharField(max_length=255)
	prénom = models.CharField(max_length=255)
	adresse_1 = models.CharField(max_length=255)
	adresse_2 = models.CharField(max_length=255)
	adresse_3 = models.CharField(max_length=255)
	adresse_4 = models.CharField(max_length=255)
	code_postal = models.IntegerField()
	ville = models.CharField(max_length=255)
	pays = models.CharField(max_length=255)
	npai = models.BooleanField(default=False)
	date_de_naissance = models.DateField()
	profession = models.CharField(max_length=255)
	tel_portable = models.CharField(max_length=255)
	tel_bureau = models.CharField(max_length=255)
	tel_domicile = models.CharField(max_length=255)
	email = models.CharField(max_length=255)
	mandats = models.CharField(max_length=255)
	commune = models.CharField(max_length=255)

	def __str__(self):
		return ('%s %s') % (self.prénom, self.nom)