from django.contrib import admin
from django.urls import path
from . import views


urlpatterns = [
    path('',views.Index.as_view(), name='home'),
    path('item-create', views.item_create, name='item-create'),
    path('item-update/<str:pk>', views.item_update, name='item-update'),
    path('item-delete/<str:pk>', views.item_delete, name='item-delete'),
    path('category-create', views.category_create, name='category-create'),
    path('category-update/<str:pk>', views.category_update, name='category-update'),
    path('category-delete/<str:pk>', views.category_delete, name='category-delete'),
]