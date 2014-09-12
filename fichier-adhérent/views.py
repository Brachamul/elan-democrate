from django.shortcuts import get_object_or_404, render, render_to_response
from django.http import HttpResponseRedirect, HttpResponse, HttpRequest
from django.template import RequestContext
from django.core.exceptions import ObjectDoesNotExist
from django.contrib.auth.models import User
from django.conf import settings

from .models import *
from .forms import *



def televersement_du_fichier_adherent(request):
	if request.user.has_perm('fichier-adhérent.peut_televerser'):
		if request.method == "POST":
			upload_form = TéléversementDuFichierAdhérentForm(request.POST, request.FILES)
			if upload_form.is_valid():
				fichier = request.FILES['fichier_csv']
				importateur = request.user
				slug = request.POST.get('slug')
				fichier.name = ('fichiers_adherents/' + slug + '.csv')
				nouveau_fichier = FichierAdhérents(importateur=importateur, fichier_csv=fichier, slug=slug)
				nouveau_fichier.save()
				traitement_du_fichier(nouveau_fichier)
				return HttpResponseRedirect('/')
			else:
				print (upload_form.errors)
				print (request.FILES)
				return HttpResponseRedirect('/')
		else:
			upload_form = TéléversementDuFichierAdhérentForm()
			return render(request, 'fichier-adhérent/upload.html', {'upload_form': upload_form})
	else:
		return HttpResponse("Vous n'avez pas les droits d'accès au téléversement du fichier adhérents.")



def traitement_du_fichier(fichier):
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