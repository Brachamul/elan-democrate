from django.contrib import admin

from .models import *



class AdherentDuFichierInline(admin.TabularInline):
	# For each feature, display development projects that can improve it
	model = AdhérentDuFichier
	fk_name = 'fichier'
	extra = 0

class FichierAdhérentsAdmin(admin.ModelAdmin):
	model = FichierAdhérents
	inlines = [AdherentDuFichierInline, ]

admin.site.register(FichierAdhérents, FichierAdhérentsAdmin)



class AdhérentDuFichierAdmin(admin.ModelAdmin):
	model = AdhérentDuFichier
	list_display = ("__str__", "num_adhérent", "adhérent", "fichier")

admin.site.register(AdhérentDuFichier, AdhérentDuFichierAdmin)



class AdhérentAdmin(admin.ModelAdmin):
    model = Adhérent
    list_display = ("num_adhérent", "nom", "prénom", "fédération", "email", "importé_par_le_fichier")

admin.site.register(Adhérent, AdhérentAdmin)