from django.shortcuts import render
from aggregateur.views import aggregateur

def accueil(request):
	return render( request, 'accueil/accueil.html', {
		'message_accueil' : 'accueil/message_accueil.html',
		'aggregateur': aggregateur(request, "fil"),
		})
