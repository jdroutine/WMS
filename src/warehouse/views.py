from django.shortcuts import render,redirect
from .models import Item
from .forms import  ItemCreateForm

# Create your views here.


def home(request):
    title = 'Welcome on our ste!'
    form = 'Fuck PiS'
    context = {
        "title": title,
    }
    return render(request, "home.html", context)


def list_items(request):
    title = 'List of items'
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
        return redirect('/list_items')
    context = {
        "form": form,
        "title": "Add item",
    }
    return render(request, "add_item.html", context)
