from django.shortcuts import render
from django.views.generic import CreateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy

from .models import Reservation
# Create your views here.

class CreateReservation(LoginRequiredMixin, CreateView):
    model = Reservation
    fields = "__all__"
    success_url = reverse_lazy('foods:home')