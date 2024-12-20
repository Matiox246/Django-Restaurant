from typing import Any
from django.db.models.query import QuerySet
from django.shortcuts import render
from blog.models import Blog
from django.views.generic import ListView
from django.contrib.auth.mixins import LoginRequiredMixin
# Create your views here.


class BLogListView(LoginRequiredMixin,ListView):
    model = Blog
    template_name = 'registration/user_blogs.html'
    context_object_name = 'accountblogs'

    def get_queryset(self):
        if self.request.user.is_superuser:
            return Blog.objects.all()
        else:
            return Blog.objects.filter(author=self.request.user)

    

