from django import forms
from django.contrib.auth.models import User
from .models import Property

class PropertyForm(forms.ModelForm):
    class Meta:
        model = Property
        exclude=['user']
        widgets = {
            'proname': forms.TextInput(attrs={'class': 'form-control','placeholder':'eg:Guntur,vizag'}),
            'type': forms.Select(attrs={'class': 'form-control',}),
            'city': forms.TextInput(attrs={'class': 'form-control','placeholder':'eg:Guntur,vizag'}),
            'location': forms.TextInput(attrs={'class': 'form-control','placeholder':'eg:MVP colony,A.T agraharam'}),
            'plan': forms.Select(attrs={'class': 'form-control'}),
        }