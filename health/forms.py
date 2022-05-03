from django.forms import ModelForm
from .models import Health
from django import forms

class TimeInput(forms.TimeInput):
    input_type = 'time'

class HealthForm(ModelForm):
    class Meta:
        model = Health
        fields = '__all__'
        widgets = {
                'time_to_take': TimeInput(),
                'email': forms.EmailInput,
                }
