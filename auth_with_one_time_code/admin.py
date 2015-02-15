from django.contrib import admin

from .models import *

# Register your models here.

class CredentialsAdmin(admin.ModelAdmin):
	model = Credentials
	list_display = ("user", "email", "code", "date", "attempts")

admin.site.register(Credentials, CredentialsAdmin)

class EmailConfirmationInstanceAdmin(admin.ModelAdmin):
    model = EmailConfirmationInstance
    list_display = ("adherent", "email", "code", "date")

admin.site.register(EmailConfirmationInstance, EmailConfirmationInstanceAdmin)