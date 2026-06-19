
from django.contrib import admin
from django.urls import path,include
from django.conf import settings
from django.conf.urls.static import static


from .import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('accounts.urls' , namespace='accounts')),
    path('', views.index, name='index'),
    path('blog/', include('blog.urls', namespace='blog')),
    path('about/', include('about.urls', namespace='about')),
    path('contact/', include('contact.urls', namespace='contact')),
    path('project/', include('project.urls', namespace='project')),




    path('<int:input>', views.angka),
    path('<str:huruf>', views.huruf),
    path('<slug:tangkap>', views.tangkap),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

