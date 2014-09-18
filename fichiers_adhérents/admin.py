from django.contrib import admin

from .models import *



class FichierAdhérentsAdmin(admin.ModelAdmin):
	model = FichierAdhérents

admin.site.register(FichierAdhérents, FichierAdhérentsAdmin)



class AdhérentDuFichierAdmin(admin.ModelAdmin):
	model = AdhérentDuFichier
	list_display = ("__str__", "num_adhérent", "adhérent", "fichier")

admin.site.register(AdhérentDuFichier, AdhérentDuFichierAdmin)



class AdhérentAdmin(admin.ModelAdmin):
    model = Adhérent
    list_display = ("num_adhérent", "nom", "prénom", "fédération", "importé_par_le_fichier")

admin.site.register(Adhérent, AdhérentAdmin)