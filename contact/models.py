from django.db import models

# Create your models here.

class kontak(models.Model):
    nama = models.CharField(max_length=50)
    no_hp = models.CharField(max_length=12)
    email = models.EmailField()
    pesan = models.TextField()

    def __str__(self):
        return "{}.{}.{}".format(self.nama,self.no_hp,self.email)
