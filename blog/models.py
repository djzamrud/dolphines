from django.db import models

# Create your models here.

class Post(models.Model):

    # Choicess
    class CategoryChoices(models.TextChoices):
        BLOG = 'blog', 'Blog'
        ARTIKEL = 'artikel', 'Artikel'
        BERITA = 'berita', 'Berita'

    title = models.CharField(max_length=255)
    body = models.TextField()
    category = models.CharField(
        max_length=20,
        choices=CategoryChoices.choices,
        default=CategoryChoices.ARTIKEL,
    )

    
    def __str__(self):
        return "{}.".format(self.title)