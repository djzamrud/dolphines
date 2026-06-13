from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import RegisterForms

# Create your views here.


def register_view(request):
    if request.method == 'POST':
        form = RegisterForms(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'akun {username} berhasil dibuat! Silahkan login.')
            return redirect('login')
    else:
        form = RegisterForms()

    return render (request, 'accounts/register.html', {'form' : form})

def login(request):

    return render(request, 'accounts/login.html',)

