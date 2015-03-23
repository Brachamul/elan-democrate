from django.shortcuts import render
from membres.views import carte_profil
from aggregateur.views import aggregateur

def accueil(request):
	return render( request, 'accueil/accueil.html', {
	#	'carte_profil': carte_profil(request),
		'message_accueil' : 'accueil/message_accueil.html',
		'aggregateur': aggregateur(request, "fil"),
		})
