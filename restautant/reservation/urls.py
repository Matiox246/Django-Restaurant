from django.urls import path
from . import views


app_name = "reservation"

urlpatterns = [
    path("", views.CreateReservation.as_view(), name="reservation")
]