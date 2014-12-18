from django.contrib import admin

from .models import *

# Register your models here.

class CredentialsAdmin(admin.ModelAdmin):
	model = Credentials
	list_display = ("user", "email", "code", "date", "attempts")

admin.site.register(Credentials, CredentialsAdmin)