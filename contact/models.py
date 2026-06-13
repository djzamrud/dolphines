from django.db import models

# Create your models here.

class kontak(models.Model):
    nama = models.CharField(max_length=30)
    hp = models.CharField(max_length=12)
    email = models.EmailField()

    def __str__(self):
        return "{}.{}.{}".format(self.nama,self.hp,self.email)
