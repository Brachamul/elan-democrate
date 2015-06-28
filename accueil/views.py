from django.shortcuts import render
from aggregateur.views import aggregateur

def accueil(request, page_number=1, fil=None):
	return render( request, 'accueil/accueil.html', {
		'message_accueil' : 'accueil/message_accueil.html',
		'aggregateur': aggregateur(request, page_number=page_number, fil=fil),
		'page_title': "Accueil",
		})
