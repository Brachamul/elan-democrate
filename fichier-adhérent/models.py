from django.db import models

import os
from django.utils.text import slugify

from django.contrib.auth.models import User



class FichierAdhérents(models.Model):

	importé_à_date = models.DateTimeField(auto_now_add=True)
	importateur = models.ForeignKey(User)
	fichier_csv = models.FileField(upload_to='fichiers-adherents/')

	def __str__(self):
		return "Fichier chargé le %s par %s" % (str(self.importé_à_date), str(self.importateur))

	class Meta:
		verbose_name_plural = 'fichiers adhérents'
		permissions = 'fichier-adhérent.peut_televerser'


class AdhérentDuFichier(models.Model):

	class Meta:
		verbose_name_plural = "adhérents du fichier"

	fichier_adhérents = models.ForeignKey(FichierAdhérents)
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
		return self.num_adhérent

#	class Adhérent(models.Model):
#		fédération = models.IntegerField()
#		date_première_adhésion = models.DateField()
#		date_dernière_cotisation = models.DateField()
#		num_adhérent = models.IntegerField()
#		genre = models.CharField()
#		nom = models.CharField()
#		prénom = models.CharField()
#		adresse_1 = models.CharField()
#		adresse_2 = models.CharField()
#		adresse_3 = models.CharField()
#		adresse_4 = models.CharField()
#		code_postal = models.IntegerField()
#		ville = models.CharField()
#		pays = models.CharField()
#		npai = models.BooleanField()
#		date_de_naissance = models.DateField()
#		profession = models.CharField()
#		tel_portable = models.CharField()
#		tel_bureau = models.CharField()
#		tel_domicile = models.CharField()
#		email = models.CharField()
#		mandats = models.CharField()
#		commune = models.CharField()






#	from django.core.exceptions import ValidationError
#	import os

#	class Item(models.Model):
#		name = models.CharField(max_length=255, unique=True)
#		description = models.TextField(max_length=255)
#	#	illustration = models.ImageField(upload_to=)
#	
#		def __str__(self):
#			return self.name
#	
#	
#	
#	class Feature(models.Model):
#		# A feature is what occupies a slot, it can be a man-made constuct or natural terrain.
#		name = models.CharField(max_length=255, unique=True)
#		description = models.TextField(max_length=255, blank=True)
#		shape = models.CharField(max_length=255, blank=True, default='30,0,61,15,31,31,0,16') # Coordinates of the HTML map polygon
#		slug = models.SlugField(max_length=255, unique=True) # Used to name image folder and as a css class for rendering
#	
#		def upload_details(instance, filename):
#			path = "features/" # Upload location
#			format = instance.slug + '.png' # Filename
#			return os.path.join(path, format)
#	
#		illustration = models.ImageField(upload_to=upload_details, blank=True)
#	
#		def __str__(self):
#			return self.name
#	
#	
#	
#	class DevelopmentProject(models.Model):
#		# Development projects can be applied to features in order to improve them.
#		was = models.ForeignKey(Feature, related_name='Project Source')
#		becomes = models.ForeignKey(Feature, related_name='Project Result')
#		required_materials = models.ManyToManyField(Item, through='RequiredMaterial')
#	#	illustration = models.ImageField(upload_to=)
#	
#		def development_project(self):
#			return ("[%s] ⇒ [%s]" % (str(self.was), str(self.becomes)))
#	
#		def types_of_materials_needed(self):
#			return ",\n".join([r.name for r in self.required_materials.all()])
#	
#	
#	
#	def validate_material_quantity(value):
#		if value % 10 != 0:
#			raise ValidationError('Please input a multiple of 10.')
#	
#	class RequiredMaterial(models.Model):
#		development_project = models.ForeignKey(DevelopmentProject)
#		item = models.ForeignKey(Item)
#		quantity = models.PositiveSmallIntegerField(default=0, validators=[validate_material_quantity], blank=True)
#	
#		def __str__(self):
#			quantity_of_items = str(self.item) + ', ' + str(self.quantity)
#			return quantity_of_items