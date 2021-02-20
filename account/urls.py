from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('signup/customer', views.CustomerSignup.as_view(), name='customer-signup'),
    path('signup/seller', views.SellerSignup.as_view(), name='seller-signup'),
    path('login/customer', views.CustomerLogin.as_view(), name='customer-login'),
    path('login/seller', views.SellerLogin.as_view(), name='seller-login'),
    path('login', views.login, name='login'),
    path('signup', views.signup, name='signup'),
    path('logout', views.logout, name='logout'),
]

