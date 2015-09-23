from django import forms

from .models import *

class BetaForm(forms.ModelForm):
	class Meta:
		model = BetaCandidat
		fields = ['email', 'nom_courant', 'telephone', 'fonctions']