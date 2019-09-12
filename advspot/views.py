from django.shortcuts import render
from .models import Post


def home(request):
    context = {
        'posts': Post.objects.all()
    }
    return render(request, 'advspot/home.html', context)


def about(request):
    return render(request, 'advspot/about.html', {'title': 'About'})
