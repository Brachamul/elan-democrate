from django.shortcuts import render

def tableau_de_bord(request):
    return render(request, 'tableau_de_bord/tableau_de_bord.html')