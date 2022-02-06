from django.shortcuts import render
from .models import Item
from .forms import  ItemCreateForm

# Create your views here.


def home(request):
    title = 'Witaja na naszej stronie!'
    form = 'jakiś tam napis'
    context = {
        "title": title,
    }
    return render(request, "home.html", context)


def list_items(request):
    title = 'Lista towarów'
    queryset = Item.objects.all()
    context = {
        "title": title,
        "queryset": queryset
    }
    return render(request, "list_items.html", context)


def add_item(request):
    form = ItemCreateForm(request.POST or None)
    if form.is_valid():
        form.save()
    context = {
        "form": form,
        "title": "Dodaj towar",
    }
    return render(request, "add_item.html", context)
