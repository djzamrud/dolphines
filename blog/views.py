from django.shortcuts import render, get_object_or_404
from django.shortcuts import render
from django.db.models import Q
from .models import Post, Home

# Create your views here.

from blog import models


def index(request):

    blogs =  models.Post.objects.all()
    query = request.GET.get('q', '')

    results = Post.objects.all()
    home_data = Home.objects.first()

    if query:
        results = results.filter(
            Q(title__icontains=query) | Q(body__icontains=query)
        )

    context = {
        'home': home_data,
        'posts': results, 
        'query': query,
        'title' : 'Blog',
        'blog' : blogs
    }
    return render (request, 'blog/index.html', context)

def detail_blog(request, id):
    artikel = get_object_or_404(models.Post, id=id)
    artikel_lain = models.Post.objects.exclude(id=id).order_by('-post_at')[:5]

    context = {
        'blog' : artikel,
        'semua_blog': artikel_lain
    }

    return render (request, 'blog/detail_blog.html', context)

