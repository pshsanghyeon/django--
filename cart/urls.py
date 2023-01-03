from django.contrib import admin
from django.urls import path, include
from . import views
app_name='cart'

urlpatterns = [
    path('addcart/<pk>/<mpk>', views.addcart, name = "addcart"),
    path('remove/<pk>', views.remove, name = "remove"),
    path('cart/', views.cart, name = "cart"),
    path('buy/', views.buy, name = "buy"),
    path('cupponuse', views.cupponuse, name="cupponuse"),
]