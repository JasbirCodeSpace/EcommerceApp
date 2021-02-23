from django.contrib import admin
from django.urls import path
from . import views


urlpatterns = [
    path('view', views.OrderAction.as_view(), name='view-order'),
    path('', views.Orders.as_view(), name='orders'),
]