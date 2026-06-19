from django.shortcuts import render, redirect

# Create your views here.

from .models import kontak

def index(request):

    kontaks = kontak.objects.all()
    form = None

    if request.method == 'POST':
        print('POST Masuk')
        kontak.objects.create(
            nama = request.POST.get('nama'),
            no_hp = request.POST.get('no_hp'),
            email = request.POST.get('email'),
            pesan = request.POST.get('pesan'),
        )
        print("Data sukses tersimpan via ORM!")
        return redirect (request.path)
    


    context = {
        'title' : 'Contact',
        'header' : 'Contact us For help',
        'team' : 'Contact my team',
        'img_bg' : [

            ['img/dolp4.jpg', 'dolp4'],
        ],
        'contacts' : kontaks,
        'pesan' : form

    }
    return render (request, 'contact/index.html', context)