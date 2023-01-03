from django.contrib import admin
from django.urls import path, include
from . import views
app_name = "client"

urlpatterns = [
    path('signup/', views.signup, name = "signup"),
    path('cuppon/', views.cuppon, name = "cuppon"),
]