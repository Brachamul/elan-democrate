from django.contrib import admin

from .models import *



class AdherentDuFichierInline(admin.TabularInline):
	# For each feature, display development projects that can improve it
	model = AdherentDuFichier
	fk_name = 'fichier'
	extra = 0

class FichierAdherentsAdmin(admin.ModelAdmin):
	model = FichierAdherents
	inlines = [AdherentDuFichierInline, ]

admin.site.register(FichierAdherents, FichierAdherentsAdmin)



class AdherentDuFichierAdmin(admin.ModelAdmin):
	model = AdherentDuFichier
	list_display = ("__str__", "num_adhérent", "adhérent", "fichier")

admin.site.register(AdherentDuFichier, AdherentDuFichierAdmin)



class AdherentAdmin(admin.ModelAdmin):
    model = Adherent
    list_display = ("num_adhérent", "nom", "prénom", "fédération", "email", "importé_par_le_fichier")

admin.site.register(Adherent, AdherentAdmin)