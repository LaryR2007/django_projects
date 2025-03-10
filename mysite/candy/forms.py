from django import forms
from .models import Candy, CandyDescription

class CandyForm(forms.ModelForm):
    class Meta: 
        model = Candy
        fields = ['name']

class CandyDescriptionForm(forms.ModelForm):
    class Meta: 
        model = CandyDescription
        fields = ['candy', 'ingredients', 'flavor']