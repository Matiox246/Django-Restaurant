from django.db import models
from django.utils import timezone
from account.models import User
from django.utils.translation import gettext as _

from ckeditor.fields import RichTextField



class Blog(models.Model):
    title = models.CharField(_("Title"), max_length=50)
    slug = models.SlugField("slug",unique=True, blank=True, null=True)
    description = models.CharField(_("Description"), max_length=100)
    content = RichTextField(config_name= "myConfig")
    author = models.ForeignKey(User, verbose_name="Author", on_delete=models.SET_NULL, null=True)
    image = models.ImageField(_("Image"), upload_to="blogs/", null=True)
    category = models.ForeignKey("Category", verbose_name="Category",related_name="blog", on_delete=models.CASCADE, blank=True, null=True)
    tags = models.ManyToManyField("Tag", verbose_name="Tags", related_name="blogs", blank=True)
    is_published = models.BooleanField("is published", default=False)
    publish_at = models.DateTimeField("publish at", null=True, blank=True)
    
    def __str__(self):
        return self.title

class Category(models.Model):
    title = models.CharField(_("Title"), max_length=50)
    slug = models.SlugField(_("Slug"))
    published_at = models.DateTimeField(_("Published at"), auto_now=False, auto_now_add=True)

    def __str__(self):
        return self.title
    

class Tag(models.Model):
    title = models.CharField(max_length=50)
    slug = models.SlugField()
    published_at = models.DateTimeField(auto_now=False, auto_now_add=True )
    update_at = models.DateTimeField(auto_now=False, auto_now_add=True)

    def __str__(self):
            return self.title


class Comment(models.Model):
     name = models.CharField("Name", max_length=100)
     email = models.EmailField("Email", max_length=254)
     message = models.TextField("Message")
     date = models.DateField("Date", auto_now=False, auto_now_add=True)
     blog = models.ForeignKey("Blog", verbose_name="blog", related_name="comments", on_delete=models.CASCADE)

     def __str__(self):
          return self.email