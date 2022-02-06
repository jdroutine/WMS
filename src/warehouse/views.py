from django.shortcuts import render
from .models import *

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
