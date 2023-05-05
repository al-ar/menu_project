from django.shortcuts import render, get_object_or_404
from .models import Menu

def index(request):
    title = get_object_or_404(Menu)
    context = {
        'title': title,
    }
    return render(request, 'menu/index.html', context)