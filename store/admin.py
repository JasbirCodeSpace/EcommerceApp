from django.contrib import admin
from .models.item import Item
from .models.category import Category
from .models.order import Order

class ItemList(admin.ModelAdmin):
    list_display = ['name', 'price', 'category']

    
class CategoryList(admin.ModelAdmin):
    list_display = ['name']

admin.site.register(Item, ItemList)
admin.site.register(Category, CategoryList)
admin.site.register(Order)