from multiselectfield import MultiSelectField

from django.db import models
# from django.utils.translation import gettext as _

# Create your models here.
class Food(models.Model):
    FOOD_TYPE = [
        ("drinks", 'drinks'),
        ("dinner", 'dinner'),
        ("lunch", 'lunch'),
    ]
    photo = models.ImageField(upload_to= 'foods/')
    name = models.CharField( max_length=100)
    description = models.CharField( max_length=50)
    price = models.FloatField()
    rate = models.IntegerField( default=5)
    time = models.IntegerField()
    pub_date = models.DateField( auto_now=False, auto_now_add=True)
    categories = MultiSelectField(choices=FOOD_TYPE, null=True)

    def __str__(self):
        return self.name
    
    