from django.contrib import admin

from .models import *

# Register your models here.

class ProfilAdmin(admin.ModelAdmin):
	model = Profil
	list_display = ("user", "adherent", "nom_courant", "notes")

admin.site.register(Profil, ProfilAdmin)