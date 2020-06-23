from django.shortcuts import render
from django.http import HttpResponse
from .models import Post
from django.contrib.auth.decorators import login_required

@login_required
def home(request):
    context = {
    'posts': Post.objects.all()
    }
    return render(request, 'posts/home.html', context)

def about(request):
    context = {'title': 'about'}
    return render(request, 'posts/about.html', context)
