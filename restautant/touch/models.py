from django.db import models
from django.utils import timezone
# Create your models here.

class ClientContact(models.Model):
    name = models.CharField(max_length=50)
    email = models.EmailField()
    message = models.TextField()
    date = models.DateTimeField(default=timezone.now, blank=True)