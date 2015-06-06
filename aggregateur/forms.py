from django import forms

from .models import *

class PostTextForm(forms.Form):
	title = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))
	content = forms.CharField(widget=forms.Textarea(attrs={'class': 'form-control'}))

class PostLinkForm(forms.Form):
	title = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))
	url = forms.URLField(widget=forms.URLInput(attrs={'class': 'form-control'}))

class CommentForm(forms.Form):
	content = forms.CharField(widget=forms.Textarea(attrs={'class': 'form-control', 'rows': 5}))