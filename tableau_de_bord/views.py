import logging
from django.conf import settings
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.core.exceptions import ObjectDoesNotExist
from django.http import HttpResponseRedirect, HttpResponse, HttpRequest
from django.shortcuts import get_object_or_404, render, render_to_response, redirect

@login_required
def tableau_de_bord(request): return render(request, 'tableau_de_bord/tableau_de_bord.html', {'page_title': "Tableau de bord"})

from mandats.models import *
from fichiers_adherents.models import *
from datascope.models import *
from membres.models import *
from aggregateur.models import *

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



# Posts de mise à jour

import datetime
def markdownify(multiple_string): return multiple_string.replace('\t', '').replace('\n', '  \n')

@login_required
def initialize_base_posts(request):

	illustration = settings.SITE_URL + "/static/images/flat_upload.png"

	chaine_actus = Channel.objects.get_or_create(name="Actualités")[0]
	chaine_actus.description = "Pour parler de l'actualité interne, nationale ou internationale."
	chaine_actus.is_official = True
	chaine_actus.is_default = True
	chaine_actus.illustration = illustration
	chaine_actus.save()

	chaine_edem = Channel.objects.get_or_create(name="Élan Démocrate")[0]
	chaine_edem.description = "Bugs, suggestions pour améliorer la plateforme, c'est ici !"
	chaine_edem.is_official = True
	chaine_edem.is_default = True
	chaine_edem.illustration = illustration
	chaine_edem.save()

	chaine_maj = Channel.objects.get_or_create(name="Notes de mise à jour")[0]
	chaine_maj.description = "Lorsque Élan Démocrate est mis à jour, les modifications sont répertoriées ici."
	chaine_maj.is_official = True
	chaine_maj.is_default = True
	chaine_maj.only_mods_can_post = True
	chaine_maj.illustration = illustration
	chaine_maj.save()

	channel = chaine_maj

	Post.objects.filter(channel=channel).delete()

	v0_7 = Post.objects.get_or_create(
		title = "Mise à jour v0.7 : chaînes privées",
		format = "TEXT",
		channel= channel,
		content = markdownify(
			"""Hello, pour la mise à jour v0.7, voici la modification principale :

			* **Chaînes privées :**
			Il est désormais possible de créer une chaîne privée et d'y inviter des membres."""),
		author = request.user,
		illustration = illustration,
		date = datetime.datetime(year=2015, month=10, day=7),
		)


	v0_6 = Post.objects.get_or_create(
		title = "Mise à jour v0.6 : inscriptions à la beta et activation des chaînes",
		format = "TEXT",
		channel= channel,
		content = markdownify(
			"""Hello, pour la mise à jour v0.6, voici les modifications principales :

			* **Inscription à la beta :**
			Il est désormais possible de renseigner le formulaire d'inscription à la beta, pour obtenir un compte et pouvoir tester Élan Démocrate.
			
			* **Activation des chaînes :**
			Les utilisateurs peuvent désormais créer des chaînes de discussion et filter les posts par chaîne."""),
		author = request.user,
		illustration = illustration,
		date = datetime.datetime(year=2015, month=9, day=25),
		)


	v0_5 = Post.objects.get_or_create(
		title = "Mise à jour v0.5 : intégration Twitter et notification de bienvenue",
		format = "TEXT",
		channel= channel,
		content = markdownify(
			"""Hello, pour la mise à jour v0.5, voici les modifications principales :
		
			* **Intégration Twitter :**
			Il est désormais possible de renseigner son nom d'utilisateur Twitter afin d'afficher son fil Twitter sur le profil Élan Démocrate.
			
			* **Notification de bienvenue :**
			Lors de la création du compte, une notification souhaite désormais la bienvenue au nouvel utilisateur et l'invite à renseigner son profil."""),
		author = request.user,
		illustration = illustration,
		date = datetime.datetime(year=2015, month=9, day=21),
		)


	v0_4 = Post.objects.get_or_create(
		title = "Mise à jour v0.4 : refonte graphique, pages semi-publiques pour partager sur les réseaux sociaux public et on peut maintenant modifier ou supprimer ses posts",
		format = "TEXT",
		channel= channel,
		content = markdownify(
			"""Hello, pour la mise à jour v0.4, voici les modifications principales :

			* **Refonte graphique :**
			Un graphisme plus aéré, plus animé et moins sombre, inspiré de [Naut](www.reddit.com/r/naut).
			
			* **Pages semi-publiques :**
			Lorsqu'on poste du texte ou un lien, on peut désormais le rendre "partageable" sur les réseaux sociaux, ce qui permet d'en afficher le titre et l'image. Le reste de la page reste caché aux utilisateurs non-authentifiés.
			
			* **Modifier et supprimer ses postsise en place des mandats :**
			C'était impossible, maintenant c'est possible."""),
		author = request.user,
		illustration = illustration,
		date = datetime.datetime(year=2015, month=9, day=13),
		)

	v0_3 = Post.objects.get_or_create(
		title = "Mise à jour v0.3 : refonte de l'authentification, amélioration du traitement du fichier adhérent, mise en place des mandats, et les responsables fédéraux ont désormais accès à leur partie du fichier",
		format = "TEXT",
		channel= channel,
		content = markdownify(
			"""Hello, pour la mise à jour v0.3, voici les modifications principales :

			* **Authentification :**
			Retravaillé en profondeur, le processus d'authentification a été simplifié et allégé. Il est désormais plus fluide et plus sécurisé. Par exemple, il devient impossible de "tester" une adresse mail pour voir si elle est reconnue par le fichier adhérent (donc pas de message du genre "nous avons bien envoyé un email à l'adresse patate@patate.com").
			
			* **Traitement automatisé du fichier adhérents :**
			Ajout d'une étape de validation : une fois qu'on a téléversé le fichier, on peut regarder le résultat de l'import avant de le charger dans la base. De plus, on peut désormais revenir en arrière en activant un ancien fichier en cas de problème.
			La visualisation du fichier avant sa mise en ligne permet de consulter le nombre de nouvelles adhésions, de réadhésions, et de pertes d'adhérents depuis le dernier fichier.
			
			* **Mise en place des mandats :**
			Lors du chargement d'un fichier adhérent, s'il y a des nouvelles fédération, des mandats sont créés, qu'on peut ensuite attribuer aux responsables fédéraux.

			* **Vues partielles du fichier :**
			Les responsables fédéraux peuvent désormais afficher le fichier adhérent, et ne voient que la fédération à laquelle ils ont accès."""),
		author = request.user,
		illustration = illustration,
		date = datetime.datetime(year=2015, month=7, day=14),
		)

	v0_2 = Post.objects.get_or_create(
		title = "Mise à jour v0.2 : notifications, illustrations et relooking des posts",
		format = "TEXT",
		channel= channel,
		content = markdownify(
			"""Hello, pour la mise à jour v0.2, voici les modifications principales :

			* **Un système de notifications a été mis en place :**
			Si vous répondez à un post ou à un commentaire, son auteur sera notifié.
			
			* **Les posts sont désormais illustrés :**
			Si le post est un lien vers un article ou une page web, il sera illustré par une image provenant de cet article ou de cette page. Si le post est un texte, il sera illustré par l'avatar de l'auteur.
			
			* **Les posts ont été relookés :** 
			Pour améliorer l'affichage sur mobile et afficher les commentaires plus clairement. """),
		author = request.user,
		illustration = illustration,
		date = datetime.datetime(year=2015, month=6, day=7)
		)[0]

	v0_2_6 = Comment.objects.get_or_create(
		parent_post = v0_2,
		content = markdownify(
			"""**Mise à jour v0.2.6 (nombreux fixes et améliorations) :**

			- Illustrations possibles sur les posts "texte"
			- Gestion des commentaires profonds
			- Ajout de liens vers le parent de chaque commentaire
			- Résolution du non-classement des posts de type "lien"
			- Rajout des couleurs alternatives pour les liens
			- Résolution du fait que les nouveaux commentaires gris ne s'affichaient
			pas en jaune
			- On peut maintenant clore les messages serveur"""),
		author = request.user,
		)[0]


	messages.success(request, "Les posts de mise à jour ont été installés ou mis à jour.")

	return redirect('tableau_de_bord')

@login_required
def delete_all_posts(request):
	Post.objects.all().delete()
	Comment.objects.all().delete()
	Vote.objects.all().delete()
	CommentVote.objects.all().delete()
	messages.success(request, "Les posts, commentaires et votes ont tous été supprimés")
	return redirect('tableau_de_bord')