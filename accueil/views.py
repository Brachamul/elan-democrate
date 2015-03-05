from django.shortcuts import render



from membres.views import carte_profil

def accueil(request):
	print ("beggining to render accueil")
	return render( request, 'accueil/accueil.html', {
# créer le module d'aggrégation de contenus
#		'afficher_l_aggregateur': afficher_l_aggregateur(request),
		'carte_profil': carte_profil(request),
		})