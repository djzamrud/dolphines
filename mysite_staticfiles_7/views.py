from django.shortcuts import render
from django.http import HttpResponse
from blog import models as blogModel

def index(request):

    blog = blogModel.Home.objects.all()

    context = {

        


        'title' : 'DJZA | Dolphines 🐬',
        'header' : 'Welcome to Mywebsite',
        'content' : blog,
        'img_logo' : [
             ['img/dolp2.jpg' , 'dolp2'], 
        ],
        

        
    }

    if request.method == 'POST':
        context = {
            'nama' : [request.POST['nama']],
            'hp' : [request.POST['hp']],
            'jumlah' : [request.POST['jumlah']],
        }
        print(request.POST['nama'])
        print(request.POST['hp'])
        print(request.POST['jumlah'])
    else:
        print('this GET')

        
    return render(request, 'index.html', context)

def angka(request, input):
    heading = '<h1>hallo ges</h1>'
    respon = f"{heading} <p>angka nya adalah:{input}</p>"
    return HttpResponse(respon)

def huruf(request, huruf):
    bisa = 'oke ini hasilnya :'
    hasil = f"{bisa} {huruf}"
    return HttpResponse(hasil)

def tangkap(request, tangkap):
    tes = "ini bisa slug:"
    bisa = f"{tes}{tangkap}"
    return HttpResponse(bisa)