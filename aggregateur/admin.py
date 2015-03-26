from django.contrib import admin

from .models import *

@admin.register(Post, Vote)
class AggregateurAdmin(admin.ModelAdmin):
	pass