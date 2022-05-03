from django import forms
from .models import Category
from shopping.models import Item

class BuyForm(forms.ModelForm):
    class Meta:
        model = Category
        exclude = ['category', 'totalCost', 'quantity', 'types']
    item = forms.ModelChoiceField(queryset=Item.objects.all())
