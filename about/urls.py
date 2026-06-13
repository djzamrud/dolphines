from django.urls import path

from about import views as viewsAbout

app_name = 'about'
urlpatterns = [
    path('', viewsAbout.index, name='index')
]