from django import forms

from car.models import Car

class CarForm(forms.ModelForm):
    class Meta:
        model = Car
        fields = ['type', 'model', 'year', 'image_url', 'price']
        widgets = {
            'image_url': forms.URLInput(attrs={'placeholder': 'https://...'}),
        }