from django import forms
from .models import Candy, CandyDescription, Color

class CandyForm(forms.ModelForm):
    class Meta: 
        model = Candy
        fields = ['name']

class CandyDescriptionForm(forms.ModelForm):
    colors = forms.ModelMultipleChoiceField(
        queryset=Color.objects.all(),
        widget=forms.CheckboxSelectMultiple,  # Allows selecting multiple colors
        required=False
    )

    class Meta:
        model = CandyDescription
        fields = ['ingredients', 'flavor', 'colors']