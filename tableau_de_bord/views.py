import logging
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.core.exceptions import ObjectDoesNotExist
from django.http import HttpResponseRedirect, HttpResponse, HttpRequest
from django.shortcuts import get_object_or_404, render, render_to_response, redirect

@login_required
def tableau_de_bord(request):
    return render(request, 'tableau_de_bord/tableau_de_bord.html', {'page_title': "Tableau de bord"})

from mandats.models import *
from fichiers_adherents.models import *
from datascope.models import *
from membres.models import *

@login_required
def initialisation_edem(request):
	if not MetaInstitution.objects.all() : # Il n'y a pas de méta-institutions, ce qui implique une base de données vierge

		# On utilise get_or_create pour créer les instances puis les réutiliser en cas d'ajout de manytomany.

		# Titres
		president					= Titre.objects.get_or_create(nom="Président(e)")[0]
		vice_pres					= Titre.objects.get_or_create(nom="Vice-président(e)")[0]
		secretaire					= Titre.objects.get_or_create(nom="Secrétaire")[0]
		tresorier					= Titre.objects.get_or_create(nom="Trésorier(ère)")[0]
		porte_parole				= Titre.objects.get_or_create(nom="Porte-parole")[0]
		membre_du_bureau			= Titre.objects.get_or_create(nom="Membre du bureau")[0]
		maire						= Titre.objects.get_or_create(nom="Maire")[0]
		adjoint_au_maire			= Titre.objects.get_or_create(nom="Adjoint(e) au maire")[0]
		conseiller_municipal		= Titre.objects.get_or_create(nom="Conseiller(ère) municipal(e)")[0]
		president_intercommunal		= Titre.objects.get_or_create(nom="Président(e) de l'intercommunalité")[0]
		vice_pres_intercommunal		= Titre.objects.get_or_create(nom="Vice-président(e) de l'intercommunalité")[0]
		conseiller_communautaire	= Titre.objects.get_or_create(nom="Conseiller(ère) communautaire")[0]
		president_departemental		= Titre.objects.get_or_create(nom="Président(e) du Conseil départemental")[0]
		vice_pres_departemental		= Titre.objects.get_or_create(nom="Vice-président(e) du Conseil départemental")[0]
		membre_comperm_depart		= Titre.objects.get_or_create(nom="Membre de la Commission permanente départementale")[0]
		conseiller_departemental	= Titre.objects.get_or_create(nom="Conseiller(ère) départemental")[0]
		president_regional			= Titre.objects.get_or_create(nom="Président(e) du Conseil régional")[0]
		vice_pres_regional			= Titre.objects.get_or_create(nom="Vice-président(e) du Conseil régional")[0]
		membre_du_bureau_regional	= Titre.objects.get_or_create(nom="Membre du Bureau régional")[0]
		conseiller_regional			= Titre.objects.get_or_create(nom="Conseiller(e) régional")[0]
		conseiller_national			= Titre.objects.get_or_create(nom="Conseiller(e) national")[0]

		# MetaInstitutions
		federation_jdem				= MetaInstitution.objects.get_or_create(nom="Fédération JDem")[0]
		federation_jdem.titres_par_defaut.add(president, secretaire, membre_du_bureau)

		federation_modem			= MetaInstitution.objects.get_or_create(nom="Fédération MoDem")[0]
		federation_jdem.titres_par_defaut.add(president, secretaire, tresorier, porte_parole, membre_du_bureau)

		institution_nationale		= MetaInstitution.objects.get_or_create(nom="Institution nationale")[0]
		institution_nationale.titres_par_defaut.add(president, vice_pres, secretaire, membre_du_bureau, conseiller_national)

		commune						= MetaInstitution.objects.get_or_create(nom="Commune")[0]
		commune.titres_par_defaut.add(maire, adjoint_au_maire, conseiller_municipal)

		interco						= MetaInstitution.objects.get_or_create(nom="Intercommunalité")[0]
		interco.titres_par_defaut.add(president_intercommunal, vice_pres_intercommunal, conseiller_communautaire)

		departement					= MetaInstitution.objects.get_or_create(nom="Département")[0]
		departement.titres_par_defaut.add(president_departemental, vice_pres_departemental, membre_comperm_depart, conseiller_departemental)

		region						= MetaInstitution.objects.get_or_create(nom="Région")[0]
		region.titres_par_defaut.add(president_regional, vice_pres_regional, membre_du_bureau_regional, conseiller_regional)

		# Institutions
		modem_national				= Institution(meta_institution=institution_nationale, nom="Mouvement Démocrate", prefixe="du").save()
		jdem_nationaux				= Institution(meta_institution=institution_nationale, nom="Jeunes Démocrates", prefixe="des").save()

		messages.success(request, "La base de données a été initialisée avec plusieurs données de départ.")
		logging.info("Injection de donnees de base concernant les mandats : OK")

	else : messages.error(request, "Il existe déjà des éléments dans la base de données.")

	return redirect('tableau_de_bord')

@login_required
def delete_all_mandates(request):
	Titre.objects.all().delete()
	MetaInstitution.objects.all().delete()
	Institution.objects.all().delete()
	Mandat.objects.all().delete()
	Detenteur.objects.all().delete()
	messages.success(request, "Les mandats ont tous été supprimés")
	return redirect('tableau_de_bord')



@login_required
def delete_all_adherents(request):
	Adherent.objects.all().delete()
	FichierAdherents.objects.all().delete()
	AdherentDuFichier.objects.all().delete()
	Profil.objects.exclude(pk=1).delete()
	Institution.objects.filter(meta_institution=MetaInstitution.objects.get(nom="Fédération JDem")).delete()
	VueFederation.objects.all().delete()
	messages.success(request, "Les adherents et fichiers ont tous été supprimés")
	return redirect('tableau_de_bord')