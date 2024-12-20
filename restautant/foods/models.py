from django.db import models
from django.utils.translation import gettext as _

# Create your models here.
class Food(models.Model):
    FOOD_TYPE = [
        ("breakfast", "صبحانه"),
        ("drink", "نوشیدنی"),
        ("dinner", "شام"),
        ("lunch", "ناهار"),
    ]
    photo = models.ImageField(_("تصویر غذا"), upload_to= 'foods/')
    name = models.CharField(_("نام غذا"), max_length=100)
    description = models.CharField(_("توضیحات"), max_length=50)
    price = models.IntegerField(_("قیمت"))
    rate = models.IntegerField(_("امتیاز"), default=5)
    time = models.IntegerField(_("زمان لازم"))
    pub_date = models.DateField(_("تاریخ انتشار"), auto_now=False, auto_now_add=True)
    type_food = models.CharField(_("نوع غذا"), max_length=10, choices=FOOD_TYPE, default="D")

    def __str__(self):
        return self.name
    
    