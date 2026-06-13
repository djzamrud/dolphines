from django.urls import path

from blog import views as viewsBlog

app_name = 'blog'
urlpatterns = [
    path('', viewsBlog.index, name='index'),
]