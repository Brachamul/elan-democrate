# -*- coding: utf-8 -*-

from django.db import models
from django.core.exceptions import ObjectDoesNotExist
import os
from django.utils.text import slugify
from django.conf import settings
from django.contrib.auth.models import User
from datetime import datetime, timedelta


class FichierAdherents(models.Model):

	date_d_import = models.DateTimeField(auto_now_add=True)
	importateur = models.ForeignKey(User)
	slug = models.SlugField(max_length=255)
	fichier_csv = models.FileField(upload_to='fichiers_adherents/')
	nombre_nouveaux_adherents = models.PositiveSmallIntegerField(null=True, blank=True, default=0)
	nombre_réadhésions = models.PositiveSmallIntegerField(null=True, blank=True, default=0)

	def adherents(self) :
		''' liste les adherents ayant été importés par ce fichier '''
		return AdherentDuFichier.objects.filter(fichier=self)

	def nouveaux_adherents(self) :
		''' liste le nombre d'adhérents qui seraient introduits par ce fichier '''
		nouveaux_adherents = []
		for adherent in self.adherents():
			if adherent.est_nouveau() : nouveaux_adherents.append(adherent)
		return nouveaux_adherents

	def adherents_maj(self) :
		''' liste le nombre d'adhérents qui ont réadhéré '''
		adherents_maj = []
		for adherent in self.adherents():
			try : adherent_actuel_correspondant = Adherent.objects.get(num_adhérent=adherent.num_adhérent)
			except Adherent.DoesNotExist : pass
			else : 
				if adherent.date_dernière_cotisation != adherent_actuel_correspondant.date_dernière_cotisation :
					# si l'adhérent existe et qu'il a réadhéré
					adherents_maj.append(adherent)
		return adherents_maj

	def date_ultime(self) :
		''' cherche la dernière date mentionnée dans le fichier '''
		latest_entry = self.adherents().latest('date_dernière_cotisation')
		return latest_entry.date_dernière_cotisation

	def jours_depuis_le_fichier_precedent(self) :
		try : date_actuelle = Adherent.objects.latest('date_dernière_cotisation').date_dernière_cotisation
		except Adherent.DoesNotExist : return False
		else :
			jours = (date_actuelle - self.date_ultime()).days
			return jours

	def __str__(self):
		return self.slug

	class Meta:
		verbose_name_plural = u'fichiers adhérents'
		permissions = (('peut_televerser', 'peut téléverser'),)
		# if request.user.has_perm('fichiers_adhérents.peut_televerser')



class Adherent(models.Model):
	# Ce profil reprend une partie des données du fichier adhérent officiel du MoDem. Il ne peut pas être modifié par l'utilisateur
	num_adhérent = models.IntegerField(primary_key=True)
	fédération = models.IntegerField(null=True, blank=True)
	date_première_adhésion = models.DateField(null=True, blank=True)
	date_dernière_cotisation = models.DateField(null=True, blank=True)
	nom = models.CharField(max_length=255, null=True, blank=True)
	prénom = models.CharField(max_length=255, null=True, blank=True)
	code_postal = models.IntegerField(null=True, blank=True)
	ville = models.CharField(max_length=255, null=True, blank=True)
	pays = models.CharField(max_length=255, null=True, blank=True)
	date_de_naissance = models.DateField(null=True, blank=True)
	profession = models.CharField(max_length=255, null=True, blank=True)
	tel_portable = models.CharField(max_length=255, null=True, blank=True)
	tel_bureau = models.CharField(max_length=255, null=True, blank=True)
	tel_domicile = models.CharField(max_length=255, null=True, blank=True)
	email = models.CharField(max_length=255, null=True, blank=True)
	mandats = models.CharField(max_length=255, null=True, blank=True)
	commune = models.CharField(max_length=255, null=True, blank=True) # Dans le cas où la personne est élu dans une autre commune que sa ville de résidence.
	importé_par_le_fichier = models.ForeignKey(FichierAdherents, null=True, blank=True, on_delete=models.SET_NULL)

	def anciennete(self): return datetime.now() - self.date_première_adhésion
	def actif(self): return (datetime.now().year - self.date_dernière_cotisation.year) > settings.DUREE_D_ACTIVITE
	def jours_depuis_la_derniere_cotisation(self): return (datetime.now().date() - self.date_dernière_cotisation).days

	def __str__(self): return '{} {}'.format(self.prénom, self.nom)


class AdherentDuFichier(models.Model):

	class Meta:
		verbose_name_plural = u"adhérents du fichier"

	fichier = models.ForeignKey(FichierAdherents)
	adhérent = models.ForeignKey(Adherent, null=True)
	fédération = models.IntegerField(null=True)
	date_première_adhésion = models.DateField(null=True)
	date_dernière_cotisation = models.DateField(null=True)
	num_adhérent = models.IntegerField(null=True)
	nom = models.CharField(max_length=255, null=True)
	prénom = models.CharField(max_length=255, null=True)
	code_postal = models.IntegerField(null=True)
	ville = models.CharField(max_length=255, null=True)
	pays = models.CharField(max_length=255, null=True)
	date_de_naissance = models.DateField(null=True)
	profession = models.CharField(max_length=255, null=True)
	tel_portable = models.CharField(max_length=255, null=True)
	tel_bureau = models.CharField(max_length=255, null=True)
	tel_domicile = models.CharField(max_length=255, null=True)
	email = models.CharField(max_length=255, null=True)
	mandats = models.CharField(max_length=255, null=True)
	commune = models.CharField(max_length=255, null=True)

	def est_nouveau(self):
		try : adherent_actuel_correspondant = Adherent.objects.get(num_adhérent=self.num_adhérent)
		except Adherent.DoesNotExist : return True
		else : return False

	def transferer_les_donnees_dun_adherent_du_fichier(self, adherent_de_la_base):
		''' transfère les données du fichier adhérent vers la base '''
		adherent_de_la_base.fédération = self.fédération
		adherent_de_la_base.date_première_adhésion = self.date_première_adhésion
		adherent_de_la_base.date_dernière_cotisation = self.date_dernière_cotisation
		adherent_de_la_base.nom = self.nom
		adherent_de_la_base.prénom = self.prénom
		adherent_de_la_base.code_postal = self.code_postal
		adherent_de_la_base.ville = self.ville
		adherent_de_la_base.pays = self.pays
		adherent_de_la_base.date_de_naissance = self.date_de_naissance
		adherent_de_la_base.profession = self.profession
		adherent_de_la_base.tel_portable = self.tel_portable
		adherent_de_la_base.tel_bureau = self.tel_bureau
		adherent_de_la_base.tel_domicile = self.tel_domicile
		adherent_de_la_base.email = self.email
		adherent_de_la_base.mandats = self.mandats
		adherent_de_la_base.commune = self.commune
		adherent_de_la_base.importé_par_le_fichier = self.fichier
		adherent_de_la_base.save()

	def creer_un_nouvel_adherent(self):
		''' Ajoute un adhérent du fichier importé à la base '''
		nouvel_adherent = Adherent(num_adhérent=self.num_adhérent)
		self.transferer_les_donnees_dun_adherent_du_fichier(nouvel_adherent)
		nouvel_adherent.save()
	
	def mettre_a_jour_un_adherent(self):
		''' Met à jour les adhérents existants avec les données du fichier importé '''
		adherent_maj = Adherent.objects.get(num_adhérent=self.num_adhérent)
		self.transferer_les_donnees_dun_adherent_du_fichier(adherent_maj)

	def __str__(self): return ('%s %s') % (self.prénom, self.nom)