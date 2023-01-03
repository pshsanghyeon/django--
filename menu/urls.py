from django.contrib import admin
from django.urls import path, include
from . import views
app_name='menu'

urlpatterns = [
    path('sushi/', views.sushi, name="sushi"),
    path('basic/', views.basic, name="basic"),
    path('coffee/', views.coffee, name="coffee"),
    path('drink/', views.drink, name="drink"),
    path('inari/', views.inari, name="inari"),
    path('set/', views.set, name="set"),
    path('side/', views.side, name="side"),
]