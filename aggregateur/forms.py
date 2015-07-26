from django import forms

from .models import *

class PostTextForm(forms.Form):
	Titre = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))
	Texte = forms.CharField(widget=forms.Textarea(attrs={'class': 'form-control'}))
	Illustration = forms.CharField(widget=forms.URLInput(attrs={'class': 'form-control'}), required=False)

class PostLinkForm(forms.Form):
	Titre = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))
	Lien_URL = forms.URLField(widget=forms.URLInput(attrs={'class': 'form-control'}))

class CommentForm(forms.Form):
	content = forms.CharField(widget=forms.Textarea(attrs={'class': 'form-control', 'rows': 5}))