from django.shortcuts import render

# Create your views here.

def index(request):
    context = {
        'title' : 'My Project'
    }

    return render(request, 'project/index.html', context)