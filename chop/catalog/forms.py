from django import forms
from .models import *

class CatAnimal(forms.ModelForm):

    model = AnimalCategory
    fields = ('name')
    widgets = {'slug': forms.HiddenInput}