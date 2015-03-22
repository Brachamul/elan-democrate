from django import forms

from .models import FichierAdhérents

class TéléversementDuFichierAdhérentForm(forms.ModelForm):

	class Meta:
		model = FichierAdhérents
		fields = ('fichier_csv',)