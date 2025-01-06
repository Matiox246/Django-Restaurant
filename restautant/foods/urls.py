from django.urls import path
from .import views


app_name = "foods"

urlpatterns = [
    path("", views.food_list, name="home"),
    path("menu/", views.menu_view, name="menu"),
    path("about/", views.about_view, name="about"),
    path("staff/", views.staff_view, name="staff"),
    path("gallery/", views.gallery_view, name="gallery"),
]