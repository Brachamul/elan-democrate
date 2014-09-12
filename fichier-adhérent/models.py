from django.db import models

import os
from django.utils.text import slugify

from django.contrib.auth.models import User



class FichierAdhérents(models.Model):

	importé_à_date = models.DateTimeField(auto_now_add=True)
	importateur = models.ForeignKey(User)
	slug = models.SlugField(max_length=255)

#	def stockage_des_fichiers(instance, filename):
#		path = 'fichier-adherents/' # Upload location
#		format = str(instance.slug) + '.csv' # Le traitement du fichier dépend de son nom, ne pas modifier !
#		return os.path.join(path, format)

	fichier_csv = models.FileField(upload_to='fichiers_adherents/')

	def __str__(self):
		return self.slug

	class Meta:
		verbose_name_plural = 'fichiers adhérents'
		permissions = (('peut_televerser', 'peut téléverser'),)



class AdhérentDuFichier(models.Model):

	class Meta:
		verbose_name_plural = "adhérents du fichier"

	fichier = models.ForeignKey(FichierAdhérents)
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
