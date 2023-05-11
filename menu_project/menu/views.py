from django.shortcuts import render


def index(request, Item=None):
    return render(request, 'menu/index.html')


def menu(request):
    return render(request, 'menu/sub.html')