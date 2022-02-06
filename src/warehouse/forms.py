from django import forms

from .models import Item


class ItemCreateForm(forms.ModelForm):
    class Meta:
        model: Item
        fields = ['item_name', 'category', 'brand', 'quantity']
