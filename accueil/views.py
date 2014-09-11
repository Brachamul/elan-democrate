from django.shortcuts import render_to_response

def accueil(request):
	return render_to_response('accueil/accueil.html')