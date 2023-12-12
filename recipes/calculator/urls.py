from django.urls import path
from calculator.views import show_recipe, home

urlpatterns = [
    path('', home, name='home'),
    path('<str:dish_name>/', show_recipe, name='show_recipe'),
]