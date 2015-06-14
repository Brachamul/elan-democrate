import logging
from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404, render, render_to_response, redirect
from django.http import HttpResponseRedirect, HttpResponse, HttpRequest
from django.template import RequestContext
from django.core.exceptions import ObjectDoesNotExist
from django.contrib.auth.models import User
from django.contrib import messages
from django.conf import settings

import sys

from .models import *
from .forms import *

@login_required
def televersement(request):
	if request.user.has_perm('fichiers_adhérents.peut_televerser'):
		if request.method == "POST":
			upload_form = TéléversementDuFichierAdhérentForm(request.POST, request.FILES)
			if upload_form.is_valid():
				logging.info("Un nouveau fichier adhérent a été téléversé par {user}.".format(user=request.user).encode('utf8'))
				fichier = request.FILES['fichier_csv']
				importateur = request.user
				slug = request.POST.get('slug')
				fichier.name = ('fichiers_adherents/' + slug + '.csv') # renomme le fichier grâce au slug
				nouveau_fichier = FichierAdhérents(importateur=importateur, fichier_csv=fichier, slug=slug) # rattache le fichier à la base des fichiers importés
				nouveau_fichier.save()
				return redirect('previsualisation_du_fichier_adhérent', fichier_id=nouveau_fichier.id )
			else:
				return render(request, 'fichiers_adherents/upload.html', {'upload_form': upload_form})
		else:
			upload_form = TéléversementDuFichierAdhérentForm()
			return render(request, 'fichiers_adherents/upload.html', {'upload_form': upload_form})
	else:
		messages.error(request, "Vous n'avez pas les droits d'accès au téléversement du fichier des adhérents.")
		return redirect('accueil')

@login_required
def previsualisation(request, fichier_id):
	fichier = FichierAdhérents
	return render(request, 'fichiers_adherents/previsualisation.html', {'fichierload_form': upload_form})
#	importation(nouveau_fichier) # Importe les données du fichier dans la base "AdhérentDuFichier"
#	adhérents_importés = AdhérentDuFichier.objects.filter(fichier=nouveau_fichier) # prend tous les adhérents présents dans le nouveau fichier
#	logging.info("Le fichier contient les données de {nombre} adhérents.".format(nombre=adhérents_importés.count()).encode('utf8'))
#	nombre_nouveaux_adherents = 0
#	nombre_réadhésions = 0
#	for adherent_du_fichier in adhérents_importés:
#		compteur = Adhérent.objects.filter(num_adhérent=adherent_du_fichier.num_adhérent).count() # compte le nombre de fois où ce numéro adhérent existe dans la base
#		if compteur == 0 : # le numéro d'adhérent n'existe pas dans la base
#			creer_un_nouvel_adherent(adherent_du_fichier) # création d'un nouvel adhérent
#			nombre_nouveaux_adherents += 1
#		elif compteur == 1 :
#			# Si l'adhérent était déjà dans la base et qu'on a une nouvelle date de dernière cotisation, on compte une réadhésion
#			adherent_maj = Adhérent.objects.get(num_adhérent=adherent_du_fichier.num_adhérent)
#			if adherent_maj.date_dernière_cotisation != adherent_du_fichier.date_dernière_cotisation :
#				nombre_réadhésions += 1
#			mettre_a_jour_un_adherent(adherent_du_fichier)
#
#	logging.info("Nouveaux adhérents : %d" % (nombre_nouveaux_adherents).encode('utf8'))
#	logging.info("Réadhésions : %d" % (nombre_réadhésions).encode('utf8'))
#	return render(request, 'fichiers_adherents/traitement.html', {
#		'fichier': nouveau_fichier,
#		'nombre_nouveaux_adherents': nombre_nouveaux_adherents,
#		'nombre_réadhésions': nombre_réadhésions,
#		})

import csv
import datetime

def importation(fichier):
	# Lis le fichier CSV importé et crée une instance AdhérentDuFichier pour chacun d'entre eux
	with open(settings.MEDIA_ROOT + '/' + fichier.fichier_csv.name, encoding="cp1252", newline='') as fichier_ouvert:
		lecteur = csv.DictReader(fichier_ouvert, delimiter=";")
		for row in lecteur:
			nouvel_adherent = AdhérentDuFichier(fichier=fichier)
			nouvel_adherent.fédération = row['Fédération']
			nouvel_adherent.date_première_adhésion = process_csv_date(row['Date première adhésion'])
			nouvel_adherent.date_dernière_cotisation = process_csv_date(row['Date dernière cotisation'])
			nouvel_adherent.num_adhérent = row['Num adhérent']
			nouvel_adherent.nom = row['Nom']
			nouvel_adherent.prénom = row['Prénom']
			nouvel_adherent.code_postal = row['Code postal']
			nouvel_adherent.ville = row['Ville']
			nouvel_adherent.pays = row['Pays']
			nouvel_adherent.date_de_naissance = process_csv_date(row['Date de naissance'])
			nouvel_adherent.profession = row['Profession']
			nouvel_adherent.tel_portable = row['Tel portable']
			nouvel_adherent.tel_bureau = row['Tel bureau']
			nouvel_adherent.tel_domicile = row['Tel domicile']
			nouvel_adherent.email = row['Email']
			nouvel_adherent.mandats = row['Mandats'].replace("\n", ", ")
			nouvel_adherent.commune = row['Commune']
			nouvel_adherent.save()



def process_csv_date(csv_date):
	if csv_date : 
		processed_date = datetime.datetime.strptime(csv_date, '%m/%d/%Y').date()
		return processed_date
	else : return None



def creer_un_nouvel_adherent(adherent_du_fichier):
	# Ajoute les nouveaux adhérents au fichier Adhérent
	logging.info("Importation de %s %s, nouvel adhérent numéro %d." % (adherent_du_fichier.prénom, adherent_du_fichier.nom, adherent_du_fichier.num_adhérent).encode('utf8'))
	fichier = adherent_du_fichier.fichier
	nouvel_adherent = Adhérent(num_adhérent=adherent_du_fichier.num_adhérent)
	copier_les_donnees_de_l_adherent(nouvel_adherent, adherent_du_fichier, fichier)
	nouvel_adherent.save()
	fichier.nombre_nouveaux_adherents += 1
	fichier.save()

def mettre_a_jour_un_adherent(adherent_du_fichier):
	# Met à jour les adhérents existants avec les nouvelles données
	adherent_maj = Adhérent.objects.get(num_adhérent=adherent_du_fichier.num_adhérent)
	copier_les_donnees_de_l_adherent(adherent_maj, adherent_du_fichier, adherent_du_fichier.fichier)
	adherent_maj.save()


def copier_les_donnees_de_l_adherent(nouvel_adherent, adherent_du_fichier, fichier):
	nouvel_adherent.fédération = adherent_du_fichier.fédération
	nouvel_adherent.date_première_adhésion = adherent_du_fichier.date_première_adhésion
	nouvel_adherent.date_dernière_cotisation = adherent_du_fichier.date_dernière_cotisation
	nouvel_adherent.nom = adherent_du_fichier.nom
	nouvel_adherent.prénom = adherent_du_fichier.prénom
	nouvel_adherent.code_postal = adherent_du_fichier.code_postal
	nouvel_adherent.ville = adherent_du_fichier.ville
	nouvel_adherent.pays = adherent_du_fichier.pays
	nouvel_adherent.date_de_naissance = adherent_du_fichier.date_de_naissance
	nouvel_adherent.profession = adherent_du_fichier.profession
	nouvel_adherent.tel_portable = adherent_du_fichier.tel_portable
	nouvel_adherent.tel_bureau = adherent_du_fichier.tel_bureau
	nouvel_adherent.tel_domicile = adherent_du_fichier.tel_domicile
	nouvel_adherent.email = adherent_du_fichier.email
	nouvel_adherent.mandats = adherent_du_fichier.mandats
	nouvel_adherent.commune = adherent_du_fichier.commune
	nouvel_adherent.importé_par_le_fichier = adherent_du_fichier.fichier
	nouvel_adherent.save()