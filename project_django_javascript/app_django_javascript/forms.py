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


class AjaxCreateForm(ModelForm):
    class Meta:
        model = AjaxCreate
        exclude = [
            'date_created',
        ]


class CarModelOrderForm(ModelForm):
    class Meta:
        model = DropdownOrder
        fields = '__all__'

        def __init__(self, *args, **kwargs):
            super().__init__(*args, **kwargs)
            self.fields['model'].queryset = DropdownCarModel.objects.none()

            if 'car' in self.data:
                try:
                    car_id = int(self.data.get('car'))
                    self.fields['model'].queryset = DropdownCarModel.objects.filter(car_id=car_id).order_by('name')
                except (ValueError, TypeError):
                    pass  # invalid input from the client; ignore and fallback to empty 'model' queryset
            elif self.instance.pk:
                self.fields['model'].queryset = self.instance.car.model_set.order_by('name')
