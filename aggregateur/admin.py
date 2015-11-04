from django.contrib import admin

from .models import *

def user_str(self): return self.profil.nom_courant
User.__str__ = user_str

class PostAdmin(admin.ModelAdmin):
	readonly_fields = ('date',)

admin.site.register(Post,PostAdmin)
admin.site.register(Comment)
admin.site.register(Vote)
admin.site.register(CommentVote)
admin.site.register(Channel)
admin.site.register(WantToJoinChannel)
admin.site.register(Settings)