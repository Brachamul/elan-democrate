from django.shortcuts import get_object_or_404, render, render_to_response
from django.http import HttpResponseRedirect, HttpResponse, HttpRequest
from django.template import RequestContext
from django.core.exceptions import ObjectDoesNotExist
from django.contrib.auth.models import User
from django.conf import settings

from .models import *
from .forms import *


def televersement_du_fichier_adherent(request):
	if request.user.has_perm('fichiers_adhérents.peut_televerser'):
		if request.method == "POST":
			upload_form = TéléversementDuFichierAdhérentForm(request.POST, request.FILES)
			if upload_form.is_valid():

				fichier = request.FILES['fichier_csv']
				importateur = request.user
				slug = request.POST.get('slug')
				fichier.name = ('fichiers_adherents/' + slug + '.csv') # renomme le fichier grâce au slug
				nouveau_fichier = FichierAdhérents(importateur=importateur, fichier_csv=fichier, slug=slug) # rattache le fichier à la base des fichiers importés
				nouveau_fichier.save()

				traitement_du_fichier(nouveau_fichier) # Importe les données du fichier dans la base "AdhérentDuFichier"

				adhérents_importés = AdhérentDuFichier.objects.filter(fichier=nouveau_fichier) # prend tous les adhérents présents dans le nouveau fichier
				for adhérent in adhérents_importés:
					try:
						query = Adhérent.objects.get(num_adhérent=adhérent.num_adhérent) # regarde si le numéro d'adhérent existe déjà dans la base
					except Adhérent.DoesNotExist:
						creer_un_nouvel_adherent(adhérent) # sinon, ajoute le nouvel adhérent à la base
					else:
						# si oui, vérifier qu'il n'y a pas de mise à jour à faire ?
						adhérent.adhérent = Adhérent.objects.get(num_adhérent=adhérent.num_adhérent) # rattacher l'instance AdhérentDuFichier à son instance Adhérent

				return render(request, 'fichiers_adhérents/traitement.html', {'fichier': nouveau_fichier})

			else:
				print (upload_form.errors)
				print (request.FILES)
				return render(request, 'fichiers_adhérents/téléverser.html', {'upload_form': upload_form})
		else:
			upload_form = TéléversementDuFichierAdhérentForm()
			return render(request, 'fichiers_adhérents/téléverser.html', {'upload_form': upload_form})
	else:
		return HttpResponse("Vous n'avez pas les droits d'accès au téléversement du fichier adhérents.")



def traitement_du_fichier(fichier):
	# Lis le fichier CSV importé et crée une instance AdhérentDuFichier pour chacun d'entre eux
	import csv
	import datetime
	with open(settings.MEDIA_ROOT + '/' + fichier.fichier_csv.name) as fichier_ouvert:
		lecteur = csv.DictReader(fichier_ouvert, delimiter=";", quotechar='|')
		for row in lecteur:
			nouvel_adhérent = AdhérentDuFichier(fichier=fichier)
			nouvel_adhérent.fédération = row['Fédération']
			nouvel_adhérent.date_première_adhésion = datetime.datetime.strptime(row['Date première adhésion'], '%m/%d/%Y').date()
			nouvel_adhérent.date_dernière_cotisation = datetime.datetime.strptime(row['Date dernière cotisation'], '%m/%d/%Y').date()
			nouvel_adhérent.num_adhérent = row['Num adhérent']
			nouvel_adhérent.genre = row['Genre']
			nouvel_adhérent.nom = row['Nom']
			nouvel_adhérent.prénom = row['Prénom']
			nouvel_adhérent.adresse_1 = row['Adresse 1']
			nouvel_adhérent.adresse_2 = row['Adresse 2']
			nouvel_adhérent.adresse_3 = row['Adresse 3']
			nouvel_adhérent.adresse_4 = row['Adresse 4']
			nouvel_adhérent.code_postal = row['Code postal']
			nouvel_adhérent.ville = row['Ville']
			nouvel_adhérent.pays = row['Pays']
#			nouvel_adhérent.npai = row['NPAI'] # Ca sert à rien et le boolean marche pas, ça m'emmerde.
			nouvel_adhérent.date_de_naissance = datetime.datetime.strptime(row['Date de naissance'], '%m/%d/%Y').date()
			nouvel_adhérent.profession = row['Profession']
			nouvel_adhérent.tel_portable = row['Tel portable']
			nouvel_adhérent.tel_bureau = row['Tel bureau']
			nouvel_adhérent.tel_domicile = row['Tel domicile']
			nouvel_adhérent.email = row['Email']
			nouvel_adhérent.mandats = row['Mandats']
			nouvel_adhérent.commune = row['Commune']
			nouvel_adhérent.save()

def creer_un_nouvel_adherent(adherent_du_fichier):
	# Ajoute les nouveaux adhérents au fichier Adhérent
	nouvel_adherent = Adhérent(num_adhérent=adherent_du_fichier.num_adhérent)
	nouvel_adherent.fédération = adherent_du_fichier.fédération
	nouvel_adherent.date_première_adhésion = adherent_du_fichier.date_première_adhésion
	nouvel_adherent.date_dernière_cotisation = adherent_du_fichier.date_dernière_cotisation
	nouvel_adherent.genre = adherent_du_fichier.genre
	nouvel_adherent.nom = adherent_du_fichier.nom
	nouvel_adherent.prénom = adherent_du_fichier.prénom
	nouvel_adherent.adresse_1 = adherent_du_fichier.adresse_1
	nouvel_adherent.adresse_2 = adherent_du_fichier.adresse_2
	nouvel_adherent.adresse_3 = adherent_du_fichier.adresse_3
	nouvel_adherent.adresse_4 = adherent_du_fichier.adresse_4
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
	adherent_du_fichier.adhérent = nouvel_adherent # lie l'instance AdhérentDuFichier importé à l'instance Adhérent permanente
	adherent_du_fichier.save()