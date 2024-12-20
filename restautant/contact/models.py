from django.db import models
from django.utils import timezone
# Create your models here.

class Contact(models.Model):
    name = models.CharField("name", max_length=50)
    email = models.EmailField("email", max_length=254)
    message = models.TextField("message")
    date = models.DateTimeField("Date", auto_now=False, auto_now_add=False, default=timezone.now)

    def __str__(self):
        return self.name