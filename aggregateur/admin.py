from django.contrib import admin

from .models import *

@admin.register(Post, Vote, Comment)
class AggregateurAdmin(admin.ModelAdmin):
	pass