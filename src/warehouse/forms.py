from django import forms
from .models import Item


class ItemCreateForm(forms.ModelForm):
    class Meta:
        model = Item
        fields = ['item_name', 'category', 'brand', 'quantity']

    def clean_category(self):
        category = self.cleaned_data.get('category')
        if not category:
            raise forms.ValidationError('This field is required')
        return category

    def clean_item_name(self):
        item_name = self.cleaned_data.get('item_name')
        if not item_name:
            raise forms.ValidationError('This field is required')

        for instance in Item.objects.all():
            if instance.item_name == item_name:
                raise forms.ValidationError(item_name + ' is aleready created')
        return item_name


5


class ItemSearchForm(forms.ModelForm):
    class Meta:
        model = Item
        fields = ['category', 'item_name']
