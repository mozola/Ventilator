from django import forms
from .models import TurboModel


class TurboForm(forms.ModelForm):
    class Meta:
         model=TurboModel                                     
