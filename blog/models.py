from django.db import models
from ckeditor.fields import RichTextField

# Create your models here.

class Post(models.Model):

    # Choicess
    class CategoryChoices(models.TextChoices):
        BLOG = 'blog', 'Blog'
        ARTIKEL = 'artikel', 'Artikel'
        BERITA = 'berita', 'Berita'

    title = models.CharField(max_length=255)
    body = RichTextField()
    penulis = models.CharField(max_length=50)
    image = models.ImageField(upload_to='blog/img/', blank=True, null=True)
    category = models.CharField(
        max_length=20,
        choices=CategoryChoices.choices,
        default=CategoryChoices.ARTIKEL,
    )
    post_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-post_at']

    
    def __str__(self):
        return "{}.{}.".format(self.title,self.penulis)
    

class Home(models.Model):
    nama = models.CharField(max_length=30)
    deskripsi = models.TextField(max_length=300, blank=True, null=True)
    image = models.ImageField(
        upload_to='blog/img/home', blank=True, null=True
    )
    notes = RichTextField(blank=True, null=True)

    def __str__(self):
        return "{}".format(self.nama)
