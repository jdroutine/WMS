from django.shortcuts import render, redirect
from .models import Item
from .forms import ItemCreateForm, ItemSearchForm, ItemUpdateForm

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
    form = ItemSearchForm(request.POST or None)
    queryset = Item.objects.all()
    context = {
        "title": title,
        "queryset": queryset,
        "form": form,
    }
    if request.method == 'POST':
        queryset = Item.objects.filter(category__icontains=form['category'].value(),
                                       item_name__icontains=form['item_name'].value(
        )
        )
        context = {
            "form": form,
            "title": title,
            "queryset": queryset,
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


def update_item(request, pk):
    queryset = Item.objects.get(id=pk)
    form = ItemUpdateForm(instance=queryset)
    if request.method == 'POST':
        form = ItemUpdateForm(request.POST, instance=queryset)
        if form.is_valid():
            form.save()
            return redirect('/list_items')
    context = {
        'form': form
    }
    return render(request, 'add_item.html', context)
