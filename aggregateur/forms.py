from django import forms
from django.db.models import Count

from .models import *

class PostTextForm(forms.Form):
	Titre = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))
	Texte = forms.CharField(widget=forms.Textarea(attrs={'class': 'form-control'}))
	Illustration = forms.CharField(widget=forms.URLInput(attrs={'class': 'form-control'}), required=False)
	Partageable = forms.BooleanField(widget=forms.CheckboxInput(attrs={'checked': 'checked'}), required=False)
#	Chaîne = forms.ModelChoiceField(
#		queryset=Channel.objects.all().annotate(num_subscribers=Count('subscribers')).order_by('-is_default', '-num_subscribers'),
#		widget=forms.Select(attrs={'class': 'form-control'})
#		)

class PostLinkForm(forms.Form):
	Titre = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))
	Lien_URL = forms.URLField(widget=forms.URLInput(attrs={'class': 'form-control'}))
	Partageable = forms.BooleanField(widget=forms.CheckboxInput(attrs={'checked': 'checked'}), required=False)

class CommentForm(forms.Form):
	content = forms.CharField(widget=forms.Textarea(attrs={'class': 'form-control', 'rows': 5}))

class ChannelForm(forms.ModelForm):
	class Meta:
		model = Channel
		fields = ['name', 'description', 'is_private']