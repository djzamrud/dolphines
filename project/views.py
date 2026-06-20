from django.shortcuts import render
from blog import models

# Create your views here.

def index(request):

    


    context = {
        'title' : 'My Project',
        
    }

    return render(request, 'project/index.html', context)