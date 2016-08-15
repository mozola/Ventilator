from django import forms
from .model import Parametry_wejsciowe


class Parametry_wejscioweForm(forms.ModelForm):
     class Meta:
         model=Parametry_wejsciowe   
