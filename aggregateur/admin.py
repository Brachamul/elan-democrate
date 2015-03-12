from django.contrib import admin

from .models import *

# Register your models here.



class ChannelAdmin(admin.ModelAdmin):
    model = Channel
    list_display = ("name", "official")

admin.site.register(Channel, ChannelAdmin)



class PostAdmin(admin.ModelAdmin):
	model = Post
	list_display = ("title", "score", "date", "post_type", "author", "slug")

admin.site.register(Post, PostAdmin)



class VoteAdmin(admin.ModelAdmin):
    model = Vote
    list_display = ("post", "color", "user")

admin.site.register(Vote, VoteAdmin)