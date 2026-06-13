from django.shortcuts import render

# Create your views here.

from .models import kontak

from contact import forms

def index(request):

    dataDiri = forms.data
    print(dataDiri)

    if request.method == 'POST':
        form = forms.postKontak(request.POST)
        if form.is_valid():
            form.save()
            print('halaman sukses')
    else:
        form = forms.postKontak()
    

    kontaks = kontak.objects.all()
    context = {
        'title' : 'Contact',
        'header' : 'Contact us For help',
        'team' : 'Contact my team',
        'img_bg' : [

            ['img/dolp4.jpg', 'dolp4'],
        ],
        'contacts' : kontaks,
        'personal' : dataDiri,
        'personal2' : form

    }
    return render (request, 'contact/index.html', context)