from django.db import models
from django.utils import timezone

from autoslug.fields import AutoSlugField

from django.contrib.auth.models import User



class Channel(models.Model):
	name = models.CharField(max_length=255)
	official = models.BooleanField(default=False)

	def __str__(self): return self.name



class Post(models.Model):
	format = models.CharField(max_length=255, choices=(("LINK", "link"), ("TEXT", "text")))
	title = models.CharField(max_length=144)
	slug = AutoSlugField(populate_from=('title'), unique_with='date', max_length=255)
	content = models.TextField(max_length=10000, null=True, blank=True)
	author = models.ForeignKey(User)
	channel = models.ForeignKey(Channel, null=True, blank=True)
	date = models.DateTimeField(default=timezone.now)
	health = models.IntegerField(default=0) # votes positifs - votes négatifs
	rank = models.IntegerField(default=0) # rang selon l'algorithme, prenant en compte le temps passé
	illustration = models.URLField(max_length=2000, null=True, blank=True)
	def __str__(self): return self.title



class Vote(models.Model):
	user = models.ForeignKey(User)
	post = models.ForeignKey(Post)
	color = models.CharField(max_length=24, choices=(("POS", "positif"), ("NEG", "négatif"), ("NEU", "neutre")))
	def __str__(self): return self.color

class LastRanking(models.Model):
	date = models.DateTimeField()



class Comment(models.Model):

	content = models.TextField(max_length=10000)
	author = models.ForeignKey(User)
	date = models.DateTimeField(default=timezone.now)
	last_edit = models.DateTimeField(auto_now=True)
	parent_post = models.ForeignKey(Post, null=True, blank=True)
	parent_comment = models.ForeignKey('self', null=True, blank=True)
	deleted = models.BooleanField(default=False)
	health = models.IntegerField(default=0) # votes positifs - votes négatifs
	rank = models.IntegerField(default=0) # rang selon l'algorithme, prenant en compte le temps passé

	def __str__(self): return self.content

	def post_racine(self):
		'''récupère le post auquel ce commentaire est rattaché'''
		parent_post = None
		comment = self
		while parent_post == None :
			parent_post = comment.parent_post
			if not parent_post : comment = comment.parent_comment
		return parent_post

	def profondeur(self):
		'''renvoie le niveau de profondeur de se post par rapport à sa racine'''
		profondeur = 0
		parent_post = None
		comment = self
		while parent_post == None :
			profondeur += 1
			parent_post = comment.parent_post
			if not parent_post : comment = comment.parent_comment
		return profondeur


class CommentVote(models.Model):
	user = models.ForeignKey(User)
	comment = models.ForeignKey(Comment)
	color = models.CharField(max_length=24, choices=(("POS", "positif"), ("NEG", "négatif"), ("NEU", "neutre")))
	def __str__(self): return self.color