from django.contrib import admin
from django.urls import path
from . import views


urlpatterns = [
    path('', views.Cart.as_view(), name='cart'),
    path('checkout', views.CheckOut.as_view(), name='checkout'),
]