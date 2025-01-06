from django.urls import path
from .views import ContactCreateView


app_name = "touch"

urlpatterns = [
    path("", ContactCreateView.as_view(), name="contact"),
]