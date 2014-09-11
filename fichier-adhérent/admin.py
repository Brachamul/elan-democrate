from django.contrib import admin

from .models import *



class FichierAdhérentsAdmin(admin.ModelAdmin):
	model = FichierAdhérents

admin.site.register(FichierAdhérents, FichierAdhérentsAdmin)



class AdhérentDuFichierAdmin(admin.ModelAdmin):
    model = AdhérentDuFichier

admin.site.register(AdhérentDuFichier, AdhérentDuFichierAdmin)
