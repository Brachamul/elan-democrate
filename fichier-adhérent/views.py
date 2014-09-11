from django.shortcuts import get_object_or_404, render, render_to_response
from django.http import HttpResponseRedirect, HttpResponse, HttpRequest
from django.template import RequestContext
from django.core.exceptions import ObjectDoesNotExist

from django.contrib.auth.models import User

from .models import *
from .forms import *



def televersement_du_fichier_adherent(request):
	if request.user.has_perm('fichier-adhérent.peut_televerser'):
		if request.method == "POST":
			upload_form = TéléversementDuFichierAdhérentForm(request.POST, request.FILES)
			if upload_form.is_valid():
				fichier_en_lecture = request.FILES['fichier_csv'].read()
				nom_du_fichier = request.FILES['fichier_csv'].name
				importateur = request.user
				traitement_du_fichier(fichier_en_lecture, nom_du_fichier, importateur)
				return HttpResponseRedirect('/fichier-adherent/')
			else:
				print (upload_form.errors)
				print (request.FILES)
				return HttpResponseRedirect('/fichier-adherent/televerser')
		else:
			upload_form = TéléversementDuFichierAdhérentForm()
			return render(request, 'upload.html', {'upload_form': upload_form})
	else:
		return HttpResponse("Vous n'avez pas les droits d'accès au téléversement du fichier adhérents.")



def traitement_du_fichier(fichier_en_lecture, nom_du_fichier, importateur):
	nouveau_fichier = FichierAdhérents(importateur=importateur, fichier_csv=nom_du_fichier)
	nouveau_fichier.save()
	import csv
	lecteur = csv.reader(fichier_en_lecture, delimiter=",", quotechar='|')
	for row in lecteur:
		nouvel_adhérent = AdhérentDuFichier()
		nouvel_adhérent['fichier_adhérents'] = nouveau_fichier
		column_counter = 0
		nouvel_adhérent['fédération'] = row[column_counter]
		column_counter += 1
		nouvel_adhérent['date_première_adhésion'] = row[column_counter]
		column_counter += 1
		nouvel_adhérent['date_dernière_cotisation'] = row[column_counter]
		column_counter += 1 
		nouvel_adhérent['num_adhérent'] = row[column_counter]
		column_counter += 1 
		nouvel_adhérent['genre'] = row[column_counter]
		column_counter += 1 
		nouvel_adhérent['nom'] = row[column_counter]
		column_counter += 1 
		nouvel_adhérent['prénom'] = row[column_counter]
		column_counter += 1 
		nouvel_adhérent['adresse_1'] = row[column_counter]
		column_counter += 1 
		nouvel_adhérent['adresse_2'] = row[column_counter]
		column_counter += 1 
		nouvel_adhérent['adresse_3'] = row[column_counter]
		column_counter += 1 
		nouvel_adhérent['adresse_4'] = row[column_counter]
		column_counter += 1 
		nouvel_adhérent['code_postal'] = row[column_counter]
		column_counter += 1 
		nouvel_adhérent['ville'] = row[column_counter]
		column_counter += 1 
		nouvel_adhérent['pays'] = row[column_counter]
		column_counter += 1 
		nouvel_adhérent['npai'] = row[column_counter]
		column_counter += 1 
		nouvel_adhérent['date_de_naissance'] = row[column_counter]
		column_counter += 1
		nouvel_adhérent['profession'] = row[column_counter]
		column_counter += 1 
		nouvel_adhérent['tel_portable'] = row[column_counter]
		column_counter += 1 
		nouvel_adhérent['tel_bureau'] = row[column_counter]
		column_counter += 1 
		nouvel_adhérent['tel_domicile'] = row[column_counter]
		column_counter += 1 
		nouvel_adhérent['email'] = row[column_counter]
		column_counter += 1 
		nouvel_adhérent['mandats'] = row[column_counter]
		column_counter += 1 
		nouvel_adhérent['commune'] = row[column_counter]
		nouvel_adhérent.save()