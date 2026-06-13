from django.shortcuts import render

# Create your views here.

from .models import Post

def index(request):

    Posts = Post.objects.all()

    context = {
        'title' : 'Blog',
        'header' : 'Welcome to blog page',
        'content' : 'Blog is place to information for your needs',
        'img_logo' : [
             ['blog/img/dolp3.jpg' , 'dolp3'], 
        ],
        'Posin' : Posts
    }
    return render (request, 'blog/index.html', context)