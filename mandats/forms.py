from django import forms

from .models import *

class NouveauMandatForm(forms.ModelForm):
    error_css_class = 'error'
    required_css_class = 'required'
    class Meta:
        model = Detenteur
        fields = ['mandat', 'titre', 'charge', 'date_de_debut', 'date_de_fin']