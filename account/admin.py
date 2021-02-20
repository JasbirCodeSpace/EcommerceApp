from django.contrib import admin
from .models.customer import Customer
from .models.seller import Seller

class CustomerList(admin.ModelAdmin):
    list_display = ['email']

class SellerList(admin.ModelAdmin):
    list_display = ['email']

admin.site.register(Customer, CustomerList)
admin.site.register(Seller, SellerList)
