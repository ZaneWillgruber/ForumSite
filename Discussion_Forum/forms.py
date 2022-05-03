from django.forms import ModelForm
from .models import *
from django.forms import ClearableFileInput
from django import forms

class CreateInForum(ModelForm):
    class Meta:
        model = forum
        exclude = ('name', 'email', 'post_views',)
        fields = "__all__"

        def __init__(self, *args, **kwargs):
            super(CreateInForum, self).__init__(*args, **kwargs)
            self.fields['name'].disabled = True

class CreateInDiscussion(ModelForm):
    class Meta:
        model = Discussion
        fields = "__all__"
