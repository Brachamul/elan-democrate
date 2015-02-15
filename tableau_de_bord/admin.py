from django.contrib import admin

from .models import *

class EmailAdmin(admin.ModelAdmin):
    model = Email
    list_display = ("date", "template", "author", "destination")

admin.site.register(Email, EmailAdmin)