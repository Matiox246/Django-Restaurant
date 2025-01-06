from django.db import models

# Create your models here.

class Reservation(models.Model):
    name = models.CharField("name", max_length=200)
    email = models.EmailField( max_length=254)
    phone = models.CharField(max_length=20)
    number = models.IntegerField()
    date = models.CharField(max_length=50)
    time = models.CharField(max_length=50)

    def __str__(self):
        return self.name

