from django.contrib import admin
from .forms import ItemCreateForm

# Register your models here.

from .models import Item


class ItemCreateAdmin(admin.ModelAdmin):
    list_display = ['category', 'item_name', 'quantity']
    form = ItemCreateForm
    list_filter = ['category']
    search_fields = ['category', 'item_name']


admin.site.register(Item, ItemCreateAdmin)
