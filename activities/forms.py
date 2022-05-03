from django.forms import ModelForm
from .models import Activity
from django import forms

class DateTimeInput(forms.DateTimeInput):
    input_type = 'datetime-local'

class ActivityForm(ModelForm):
    class Meta:
        model = Activity
        fields = '__all__'
        exclude = ('users',)
        widgets = {
                'time_start': DateTimeInput(),
                'time_end': DateTimeInput(),
        }

class JoinForm(ModelForm):
    class Meta:
        model = Activity
        exclude = '__all__'
