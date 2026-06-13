from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
from about import models

def index (request):

    showProfile = models.Profile.objects.all()
    print(showProfile)


    context = {
        'title' : 'About',
        'header' : 'Welcome to About page',
        'content' : 'About is place to information for your needs',
        'img_logo' : [
             ['about/img/dolp4.jpg' , 'dolp4'], 
        ],
        'showAbouts' : showProfile

    }
    return render (request, 'about/index.html', context)