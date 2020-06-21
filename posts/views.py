from django.shortcuts import render
from django.http import HttpResponse
posts = [
    {
    'author': 'Amira',
    'date': '20/2/2020',
    'content': 'I am learinig how to use django framework'
    },
    {
    'author': 'Yasser',
    'date': '20/2/2020',
    'content': 'I am learinig how to use django framework'
    }
]
# Create your views here.
def home(request):
    context = {
    'posts': posts
    }
    return render(request, 'posts/home.html', context)

def about(request):
    context = {'title': 'about'}
    return render(request, 'posts/about.html', context)
