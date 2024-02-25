from django import forms
from .models import Profile

class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['username', 'email', 'age', 'password', 'first_name', 'last_name', 'profile_picture']
        widgets = {
            'password': forms.PasswordInput()  # Полето за парола да бъде от тип PasswordInput
        }