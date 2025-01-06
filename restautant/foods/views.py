from django.shortcuts import render
from .models import Food 
# Create your views here.


def get_food_list():
    food_list = Food.objects.all()
    context = {
        "foods" : food_list
        }
    return context


def food_list(request):
    context_foods = get_food_list()
    context = {
         **context_foods,
    }
    return render(request, 'foods/home.html', context)


def menu_view(request):
    context_foods = get_food_list()
    context = {
        **context_foods,
    }
    return render(request, 'foods/menu.html', context)


def about_view(request):
    context_foods = get_food_list()
    context = {
        **context_foods,
    }
    return render(request, 'foods/about.html', context)


def staff_view(request):
    context_foods = get_food_list()
    context = {
        **context_foods,
    }
    return render(request, 'foods/staff.html', context)


def gallery_view(request):
    return render(request, 'foods/gallery.html')