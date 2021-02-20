from django import forms
from django.forms import ModelForm
from .models import *


class AlertForm(ModelForm):
    class Meta:
        model = AlertModel
        fields = '__all__'
        widgets = {
            'first_name': forms.TextInput(attrs={'placeholder': '...'}),
            'last_name': forms.TextInput(attrs={'placeholder': '...'}),
        }
