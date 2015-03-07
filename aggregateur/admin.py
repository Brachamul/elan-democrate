from django.contrib import admin

from .models import *

# Register your models here.



class PostAdmin(admin.ModelAdmin):
	model = Post
	list_display = ("title", "date", "post_type", "author")

admin.site.register(Post, PostAdmin)



class TagAdmin(admin.ModelAdmin):
    model = Tag
    list_display = ("name", "official")

admin.site.register(Tag, TagAdmin)