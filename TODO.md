***
Base
====

* ~~Modifier la barre de navigation en enlevant les boutons pour les mettre sous la photo de profil~~ (2h)
* Faire fonctionner la barre de navigation proprement sur mobile
* Permettre à l'utilisateur de fermer les messages serveur
* Faire apparaitre les sous-menus de la barre de nav au survol de la souris



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



***
Mandats
=================

* ~~**Permettre la gestion de mandats JDem**~~ (4h)
* Permettre la proposition d'un mandat
* Systèmes de validation et covalidation



***
Notifications
========

* **Mettre en place un système de notifications**



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
* **Mettre en place la pagination des posts**
* ~~**Recharger le score toutes les x minutes**~~ (2h)
* Ajouter un système d'illustration des posts
* Scraper une illustration pour chaque post
* Scraper le domaine des URLs
* Déplacer la scorebox sur mobile
* Preview du post en dessous
* Guide markdown
* Bug URL du post lien
* Rendre les affichages de posts plus responsive avec la healthbox

Commentaires
--------
* ~~**Return to comment after new comment is submitted**~~
* ~~**Répondre directement à un post**~~ (2h) 
* Gérer le cas de descente à X niveaux de commentaires
* Voter sur les commentaires
* Rendre l'ajout de commentaires dynamique (js)
* Éditer les commentaires
* Supprimer son commentaire
* ~~Permettre l'édition riche de commentaires, notamment avec des retours à la ligne~~ (2h, ajout de markdown)
* Corriger la fonction de comptage des commentaires
* Déplacer la fonction de création de commentaire de la fonction générale d'affichage de post
* Bouton pour "cacher" le formulaire de réponse aux commentaires
* Ajouter un permalien
* Les commentaires gris sont pas jaunes


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



***
Fichier Adhérents
=================

* **Tester le chargement du fichier**



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