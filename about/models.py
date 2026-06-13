from django.db import models

class Profile(models.Model):
    judul = models.CharField(max_length=50)
    author = models.PositiveIntegerField(default=1)
    date = models.DateTimeField()

    def __str__(self):
        return "{}.".format(self.judul)
