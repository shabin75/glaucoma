from django import forms
from .models import Data

class DataForms(forms.ModelForm):
    img = forms.ImageField(label='')
    class Meta:
        model=Data
        fields=('img',)