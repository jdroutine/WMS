from django.shortcuts import render


# Create your views here.


def home(request):
    title = 'Witaja na naszej stronie!'
    form = 'jakiś tam napis'
    context = {
        "title": title,

    }
    return render(request, "home.html", context)
