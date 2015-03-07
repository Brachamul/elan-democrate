from django.db import models

from django.contrib.auth.models import User



class Tag(models.Model):
	name = models.CharField(max_length=255)
	official = models.BooleanField(default=False)

	def __str__(self): return self.name



class Post(models.Model):
	post_type = models.CharField(max_length=255, choices=(("LINK", "link"), ("TEXT", "text")))
	title = models.CharField(max_length=144)
	slug = models.SlugField(max_length=144)
	#autoslug
	content = models.CharField(max_length=10000)
	author = models.ForeignKey(User)
	tags = models.ManyToManyField(Tag)
	date = models.DateTimeField(auto_now=True)

	def __str__(self): return self.title