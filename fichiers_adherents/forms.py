from django import forms

from .models import FichierAdherents

class TéléversementDuFichierAdherentForm(forms.ModelForm):

	class Meta:
		model = FichierAdherents
		fields = ('fichier_csv',)