from django.contrib import admin

from .models import *

# Register your models here.

admin.site.register(MetaInstitution)
admin.site.register(Institution)
admin.site.register(Mandat)
admin.site.register(Detenteur)
admin.site.register(Titre)