from django.shortcuts import render, get_object_or_404

# Create your views here.

from blog import models


def index(request):

    blogs =  models.Post.objects.all()

    context = {
        'title' : 'Blog',
        'blog' : blogs
    }
    return render (request, 'blog/index.html', context)

def detail_blog(request, id):
    artikel = get_object_or_404(models.Post, id=id)
    artikel_lain = models.Post.objects.exclude(id=id)[:3]

    context = {
        'blog' : artikel,
        'semua_blog': artikel_lain
    }

    return render (request, 'blog/detail_blog.html', context)