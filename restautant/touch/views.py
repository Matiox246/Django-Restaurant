from django.shortcuts import render
from django.views.generic import CreateView
from django.urls import reverse_lazy

from .models import ClientContact
# Create your views here.


class ContactCreateView(CreateView):
    model = ClientContact
    fields = "__all__"
    success_url = reverse_lazy('foods:home')
