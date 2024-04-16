from django import forms
from .models import Comanda


class ComandaForm(forms.ModelForm):
    class Meta: 
        model = Comanda
        fields = ['nume_client', 'material', 'cantitate']

        