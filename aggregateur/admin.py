from django.contrib import admin

from .models import *

import user_str

class PostAdmin(admin.ModelAdmin):
	readonly_fields = ('date',)

admin.site.register(Post,PostAdmin)
admin.site.register(Comment)
admin.site.register(Vote)
admin.site.register(CommentVote)
admin.site.register(Channel)
admin.site.register(WantToJoinChannel)
admin.site.register(Settings)