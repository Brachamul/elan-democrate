***
Base
====

* ~~Modifier la barre de navigation en enlevant les boutons pour les mettre sous la photo de profil~~ (2h)
* Faire fonctionner la barre de navigation proprement sur mobile
* ~~Permettre à l'utilisateur de fermer les messages serveur~~ (1h)


***
Membres
=======

* ~~Expliquer le fonctionnement de Gravatar~~ (1h)
* Afficher le statut d'adhesion
* URL du profil par nom
* ~~Créer un membre pour chaque adhérent du fichier~~ (2h)
* ~~Nom courant default value~~
* ~~**Rendre modifiable le nom courant**~~ (1h)
* Ajouter un système de validation du nom courant
* Et au passage un système de validation des mandats
* ~~**Permettre l'édition de son profil**~~ (2h)
* Ajouter d'autres éléments au profil (badges, occupations, intérêts, compétences, ...)
* ~~Ne pas pré-écrire "None" dans la description quand il n'y en a pas~~
* Autres utilisateurs en ligne en ce moment
* Créer un processus de validation du nom courant (pour qu'il reste non-anonyme)


***
Mandats
=================

* ~~**Permettre la gestion de mandats JDem**~~ (4h)
* Permettre la proposition d'un mandat
* Systèmes de validation et covalidation



***
Notifications
========

* ~~**Mettre en place un système de notifications**~~ (32h)
* ~~Mettre tout en "vu" au chargement des notifs~~ (1h)
* ~~Générer une notif lors de la création d'un commentaire~~ (1h)
* ~~If non_vues > 0, reload, else, don't~~ (1h)
* Passer lues les notifs cliquées et afficher différemment les notifs nonlues
* **Grouper les notifs pour éviter le spam**
* Recharger occasionellement les notifs
* ~~Ne pas s'autonotifier de ses propres actions~~ (0h)


***
Messagerie
=================

* Mettre en place un système de messages privés
* Mettre en place un système de chat



***
Aggrégateur d'actualité
=======================

Posts
-----
* ~~**Mettre en place la pagination des posts**~~ (4h)
* ~~**Recharger le score toutes les x minutes**~~ (2h)
* ~~**Ajouter un système d'illustration des posts**~~ (2h)
* ~~Scraper une illustration pour chaque post~~ (1h)
* Scraper le domaine des URLs
* ~~Déplacer la scorebox sur mobile~~ (1h)
* Preview du post lors de la rédaction
* Guide markdown
* ~~Bug URL du post lien~~
* ~~Rendre les affichages de posts plus responsive avec la healthbox~~ (1h)
* ~~**Relooking complet des posts & commentaires**~~ (4h)
* **Permettre aux utilisateurs de modifier / supprimer leurs posts**
* ~~Améliorer un peu le look des posts~~ (1h)
* ~~Modifier le régex pour régler le soucis des slugs avec caractères spéciaux~~ (1h) #17
* [Gros chantier] générer les posts via JSON pour + de dynamisme
* Auto-générer un titre
* Finaliser l'intégration des vidéos et autres iframes
* ~~Ne pas afficher l'url des links (le contenu url des posts de type link)~~ (0h)
* Sauver les thumbnails d'images sur le serveur
* ~~Problème de photo qui sort du cadre sur l'affichage des posts sur mobile~~ (1h)
* ~~Add "choose illustration"~~ (1h)


Commentaires
--------
* ~~**Return to comment after new comment is submitted**~~ (2h)
* ~~**Répondre directement à un post**~~ (2h) 
* ~~Gérer le cas de descente à X niveaux de commentaires~~ (3h)
* ~~Voter sur les commentaires~~ (2h)
* ~~Éditer les commentaires~~ (2h)
* ~~Supprimer son commentaire~~ (1h)
* ~~Permettre l'édition riche de commentaires, notamment avec des retours à la ligne~~ (2h, ajout de markdown)
* Corriger la fonction de comptage des commentaires
* Déplacer la fonction de création de commentaire de la fonction générale d'affichage de post
* ~~Bouton pour "cacher" le formulaire de réponse aux commentaires~~ (0h)
* ~~Ajouter un permalien~~ (1h)
* ~~Les commentaires gris sont pas jaunes~~ (0h)
* **Déclencher les notations des commentaires de manière récurrente**
* [Gros chantier] ajout dynamique des commentaires en Ajax
* Quand on clique sur le bouton "répondre", mettre automatiquement le curseur sur la boîte de texte
* ~~Le lien vers un commentaire prend le commentaire source !~~ (1h)
* Afficher les boites de commentaire via jQuery plutôt

Chaînes
-------
* Ajouter des vues par chaîne / source / membre
* Permettre aux utilisateurs de créer des chaînes

Autres
------
* Administration des posts / chaînes
* Prévenir le double post de commentaire / actu
* Reclassement récurrent asynchrone



***
Authentification
==============

* Gérer la durée des sessions
* Ignorer les caractères "espace" dans le code d'authentification
* ~~**Enable email registration, currently there's only adherent number registration**~~ (1h)
* ~~**Gérer le cas où l'utilisateur n'est pas enregistré et entre son numéro adhérent dans connexion**~~ (1h)
* Si dans connexion on clique sur "créer un compte" lancer directement le processus d'enregistrement plutôt que rediriger
* Si un mail est envoyé pour l'enregistrement, ne pas remontrer le formulaire
* Mettre en place l'authentification par SMS
* Gérer notamment la génération automatique de profil quand on créé un utilisateur via le numéro de tel
* Ajouter du JS à l'authentification
* URLS relatives dans le backend
* ~~local_settings pour l'URL envoyé par mail pour le lien direct de connexion~~ (1h)
* ~~Incohérence des boutons "créer un compte" et "s'enregistrer"~~ (1h)
* Le champs de connexion est rempli par "None" si il ne retrouve pas d'adhérent, remplacer par rien
* **Rediriger l'enregistrement sur une feuille de création de profil**
* **Vérifier pourquoi le même code est envoyé deux fois**



***
Fichier Adhérents
=================

* ~~**Tester le chargement du fichier**~~ (2h)
* ~~résolu un problème avec des caractères spéciaux dans les noms de fichiers template~~ (1h)
* **ajouter une étape de validation par l'utilisateur entre la lecture du fichier et son ajout à la bdd**
* ajouter la dernière date d'activité du fichier au modèle
* remplacer la lecture des mandats pour faire du filtrage dessus
* ajouter une maintenance pour virer tout les trucs useless générés pendant le processus (genre les adhérents_du_fichier)



***
Tableau de Bord
===============

* Compter le nombre d'emails envoyés par utilisateur (# authentification)
* Notamment lors de l'enregistrement
* Noter les changements de mandats
* Logger les connexions de chaque user


***
Securité
========

* ~~**Secure the settings.py file**~~ (1h)
* ~~Create local_settings.py~~ (1h)
* django.middleware.security.SecurityMiddleware [ nécessite un HTTPS partout sur le domaine ]
* Prevent mass sending of email confirmation messages
* Add terms and conditions
* Remove force_connect login
* Create a role that can do everything except look at adherent data



***
Sites
=====

* Mettre en place un système de création de sites



***
Meta
====

* ~~Retirer la DB des commits~~ (1h)
* ~~Replace prints by logging or add .encode("utf-8")~~ (1h)
* ~~**Add logging**~~ (1h)