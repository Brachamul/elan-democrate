from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.core.urlresolvers import reverse
from django.core.exceptions import ObjectDoesNotExist
from django.http import HttpResponseRedirect, HttpResponse, HttpRequest, Http404
from django.shortcuts import get_object_or_404, render, render_to_response, redirect
from django.template import RequestContext
from django.views import generic
from django.views.generic import TemplateView, DetailView

from .models import *
from .forms import *

def all(request):
	# temporary catch all url for posts
	return HttpResponseRedirect('/')



### Affichage des Posts

@login_required
def afficher_le_post(request, slug):
	''' génère la page d'affichage d'un post '''
	try : post = Post.objects.get(slug=slug)
	except Post.DoesNotExist : raise Http404("Ce post n'existe pas")
	else :
		post = get_post_meta(request, post)
		post.number_of_comments = count_post_comments(post)
		if request.method == "POST":
			new_comment = Comment(content=request.POST.get('content'), author=request.user)
			parent_comment = request.POST.get('parent_comment')
			if parent_comment :
				parent_comment = Comment.objects.get(id=parent_comment)
				new_comment.parent_comment = parent_comment
			else : new_comment.parent_post = post
			new_comment.save()
			HttpResponseRedirect('#checkbox-comment-%d' % new_comment.pk)

		return render(request, 'aggregateur/afficher_le_post.html', {'post': post, 'comment_form': CommentForm()})

@login_required
def aggregateur(request, fil):
	''' génère une carte qui affiche les données des 20 derniers posts
		l'argument "fil" n'est pas opérationnel '''
	try : posts = Post.objects.all().order_by('-rank', '-health')[:100]
	except Post.DoesNotExist : return False
	else :
		for post in posts : post = get_post_meta(request, post)
		rank_posts(request) # classe les posts s'ils n'ont pas été reclassés depuis au moins 5 minutes
		return { 'posts': posts, 'template': "aggregateur/carte_aggregateur.html", }

def get_post_meta(request, post):
	post.number_of_comments = count_post_comments(post)
	if post.format == "LINK" : post.link = post.content
	else : post.link = post.slug
	try : vote = Vote.objects.get(post=post, user=request.user)
	except Vote.DoesNotExist : pass
	else : post.color = vote.color
	return post



### Traitement des votes

def vote(request, post_id, color):
	context = RequestContext(request)
	try : post = Post.objects.get(id=int(post_id))
	except Post.DoesNotExist : print("\nERROR : Post.DoesNotExist - while trying to vote")
	else:
		try : vote = Vote.objects.get(user=request.user, post=post)
		except Vote.DoesNotExist :
			# no previous votes exist, so let's make a new one
			new_vote = Vote(user=request.user, post=post, color=color)
			new_vote.save()
			endcolor = color
		else :
			# a vote exists, so let's change it
			if   vote.color == "POS" and color == "POS" : vote.color = "NEU"
			elif vote.color == "POS" and color == "NEG" : vote.color = "NEG"
			elif vote.color == "NEU" and color == "POS" : vote.color = "POS"
			elif vote.color == "NEU" and color == "NEG" : vote.color = "NEG"
			elif vote.color == "NEG" and color == "POS" : vote.color = "POS"
			elif vote.color == "NEG" and color == "NEG" : vote.color = "NEU"
			vote.save()
			endcolor = vote.color
		print ("\n---> A %s vote was cast on post n° %s" % (endcolor, post_id))
	# return the endcolor of the vote so that we can light up the up/down arrows
	return HttpResponse(endcolor)


from datetime import datetime, timedelta
from math import log

def rank_posts(request, force=False):
	''' compte le score relatif d'un post
	straight from the reddit algorithm '''
	if time_to_rerank(request) == True or force == True :
		# on classe les posts s'il n'y a pas eu de classement depuis 5 minutes
		# sauf si un post vient d'être créé, dans quel cas cette fonction est appelée avec l'argument "force"
		bayrou_2007 = datetime(2007, 4, 22) # 18% quand même !+
		for post in Post.objects.filter(date__gt=datetime.now()-timedelta(days=30)) : # on arrête de ranker les posts de + d'un mois
			healthify(post) # on recalcule le score du post
			time_since_bayrou = ( post.date - bayrou_2007 ) # quel est l'âge relatif du post ?
			time_since_bayrou = time_since_bayrou.days * 86400 + time_since_bayrou.seconds # conversion en secondes
			order = log(max(abs(post.health), 1), 10)
			sign = 1 if post.health > 0 else -1 if post.health < 0 else 0
			post.rank = round( sign * order + time_since_bayrou / 45000, 7)
			post.save()
			result = "Classement réussi !"
	else :
		result = "Le dernier classement date déjà d'il y a moins de 5 minutes."
	print (result)
	return HttpResponse(result)

def healthify(post):
	''' compte le score absolu d'un post '''
	pos = Vote.objects.filter(post=post, color="POS").count()
	neg = Vote.objects.filter(post=post, color="NEG").count()
	post.health = pos-neg
	post.save()

def time_to_rerank(request):
	try :
		last_ranking = LastRanking.objects.latest('date')
	except LastRanking.DoesNotExist :
		last_ranking = LastRanking.objects.create(date=datetime.now())
		return True
	else :
		if last_ranking.date < (datetime.now()-timedelta(minutes=5)) :
			last_ranking.date = datetime.now()
			last_ranking.save()
			return True
		else :
			return False



### Commentaires

def count_post_comments(post):
	number_of_comments = 0
	comments = Comment.objects.filter(parent_post=post)
	for comment in comments :
		number_of_comments += 1
		comments = Comment.objects.filter(parent_comment=comment)
		for comment in comments :
			number_of_comments += 1
			comments = Comment.objects.filter(parent_comment=comment)
			for comment in comments :
				number_of_comments += 1
				comments = Comment.objects.filter(parent_comment=comment)
				for comment in comments :
					number_of_comments += 1
					comments = Comment.objects.filter(parent_comment=comment)
					for comment in comments :
						number_of_comments += 1
						comments = Comment.objects.filter(parent_comment=comment)
						for comment in comments :
							number_of_comments += 1
							comments = Comment.objects.filter(parent_comment=comment)
							for comment in comments :
								number_of_comments += 1
								comments = Comment.objects.filter(parent_comment=comment)
								for comment in comments :
									number_of_comments += 1
									comments = Comment.objects.filter(parent_comment=comment)
									for comment in comments :
										number_of_comments += 1
										comments = Comment.objects.filter(parent_comment=comment)
										for comment in comments :
											number_of_comments += 1
											comments = Comment.objects.filter(parent_comment=comment)
	return number_of_comments

### Misc

@login_required
def nouveau_post(request):
	# Si le formulaire a été rempli, on le traite. Sinon, on l'affiche.
	if request.method == "POST":
		text_data = link_data = None # les données seront renvoyées au formulaire en cas d'erreur, pour éviter d'avoir à recommencer
		format = request.POST.get('format')
		if format == "TEXT" :
			title = request.POST.get('title')
			content = request.POST.get('content')
			text_data = {'title': title, 'content': content}
			if PostTextForm(request.POST).is_valid() :
				new_post = Post(
					format='TEXT',
					title=title,
					content=content,
					author=request.user,
					channel=Channel.objects.get(pk=1), # change when adding more channels
				#	illustration=
					)
				new_post.save()
				new_post_adress = "/p/" + new_post.slug
				rank_posts(request, force=True)
				print ("\n- Nouveau texte posté par %s : %s" % (request.user.username, request.POST.get('title')))
				messages.success(request, "Votre post est publié.")
				return HttpResponseRedirect(new_post_adress)
			else :
				messages.error(request, "Votre post n'a pas été publié, il semble qu'il y ait une erreur dans les champs que vous avez rempli.")

		elif format == "LINK" :
			title = request.POST.get('title')
			url = request.POST.get('url')
			link_data = {'title': title, 'url': url}
			if PostLinkForm(request.POST).is_valid() :
				new_post = Post(
					format = 'LINK',
					title=title,
					content=url,
					author=request.user,
					channel=Channel.objects.get(pk=1), # change when adding more channels
				#	illustration=
					)
				new_post.save()
				new_post_adress = "/p/" + new_post.slug
				messages.success(request, "Votre post est publié.")
				print ("\n- Nouveau lien posté par %s : %s" % (request.user.username, request.POST.get('title')))
				return HttpResponseRedirect(new_post_adress)
			else :
				messages.error(request, "Votre post n'a pas été publié, il semble qu'il y ait une erreur dans les champs que vous avez rempli.")
		else: # pas de format spécifié ?
			messages.warning(request, "Il y a un bug dans la matrice !")
		return render(request, 'aggregateur/nouveau_post.html', {'post_text_form': PostTextForm(initial=text_data), 'post_link_form': PostLinkForm(initial=link_data), })
	else :
		return render(request, 'aggregateur/nouveau_post.html', {'post_text_form': PostTextForm(), 'post_link_form': PostLinkForm(), })