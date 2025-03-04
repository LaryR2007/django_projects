from django import forms
from .models import Candy, CandyDescription

class CandyForm(forms.Form):
    class Meta: 
        mode = Candy
        fields = ['name']

class CandyDesForm(forms.Form):
    class Meta: 
        mode = CandyDescription
        fields = ['candy', 'ingredients', 'flavor']