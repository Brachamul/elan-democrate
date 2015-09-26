import logging
from django.core.management.base import BaseCommand, CommandError
from aggregateur.views import rank_posts, rank_comments

class Command(BaseCommand):
	help = 'Calcule et applique les scores des posts et des commentaires sur la base des votes des utilisateurs.'
	def handle(self, *args, **options):
		rank_posts()
		rank_comments()
		self.stdout.write("Relassement les posts : ok")