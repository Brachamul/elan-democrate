from django.db import models
from django.core.exceptions import ObjectDoesNotExist
import os
from django.utils.text import slugify

from django.contrib.auth.models import User


class FichierAdhérents(models.Model):

	date_d_import = models.DateTimeField(auto_now_add=True)
	importateur = models.ForeignKey(User)
	slug = models.SlugField(max_length=255)
	fichier_csv = models.FileField(upload_to='fichiers_adherents/')
	nombre_nouveaux_adherents = models.PositiveSmallIntegerField(null=True, blank=True, default=0)
	nombre_réadhésions = models.PositiveSmallIntegerField(null=True, blank=True, default=0)

	def adherents(self) :
		''' liste les adherents ayant été importés par ce fichier '''
		return AdhérentDuFichier.objects.filter(fichier=self)

	def nouveaux_adherents(self) :
		''' liste le nombre d'adhérents qui seraient introduits par ce fichier '''
		nouveaux_adherents = []
		for adherent in self.adherents():
			try : adherent_actuel_correspondant = Adhérent.objects.get(num_adhérent=adherent.num_adhérent)
			except Adhérent.DoesNotExist :
				nouveaux_adherents.append(adherent)
			else : print("adhérent %s trouvé dans la base" % adherent.num_adhérent)
				# si l'adhérent n'existe pas dans la base
		return nouveaux_adherents

	def adherents_maj(self) :
		''' liste le nombre d'adhérents qui ont réadhéré '''
		adherents_maj = []
		for adherent in self.adherents():
			try : adherent_actuel_correspondant = Adhérent.objects.get(num_adhérent=adherent.num_adhérent)
			except Adhérent.DoesNotExist : pass
			else : 
				if adherent.date_dernière_cotisation != adherent_actuel_correspondant.date_dernière_cotisation :
					# si l'adhérent existe et qu'il a réadhéré
					adherents_maj.append(adherent)
		return adherents_maj

	def date_ultime(self) :
		''' cherche la dernière date mentionnée dans le fichier '''
		latest_entry = self.adherents().latest('date_dernière_cotisation')
		return latest_entry.date_dernière_cotisation

	def jours_depuis_le_fichier_precedent(self):
		try : date_actuelle = Adhérent.objects.latest('date_dernière_cotisation')
		except Adhérent.DoesNotExist : return False
		else : return date_actuelle - date_ultime(self)

	def __str__(self):
		return self.slug

	class Meta:
		verbose_name_plural = 'fichiers adhérents'
		permissions = (('peut_televerser', 'peut téléverser'),)
		# if request.user.has_perm('fichiers_adhérents.peut_televerser')


class Adhérent(models.Model):
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
	importé_par_le_fichier = models.ForeignKey(FichierAdhérents, null=True, blank=True)

	def __str__(self):
		return '{} {}'.format(self.prénom, self.nom)


class AdhérentDuFichier(models.Model):

	class Meta:
		verbose_name_plural = "adhérents du fichier"

	fichier = models.ForeignKey(FichierAdhérents)
	adhérent = models.ForeignKey(Adhérent, null=True)
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

	def __str__(self):
		return ('%s %s') % (self.prénom, self.nom)