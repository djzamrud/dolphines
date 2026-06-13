from django.urls import path

from contact import views as viewsContact

app_name = 'contact'
urlpatterns = [
    path ('', viewsContact.index, name='index')
]