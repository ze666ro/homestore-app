from django.http import HttpResponse
from django.shortcuts import render
from goods.models import Categories



def index(request):


    context = {
        'title': 'Home - Главная',
        'content': "Магазин мебели HOME",
    }

    return render(request, 'main/index.html', context)


def about(request):
    context = {
        'title': 'Home - О нас',
        'content':'About Us',
        'text_on_page':' Какой же пиздатый у нас магазин '
    }
    return render(request, 'main/about.html', context)