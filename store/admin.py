from django.contrib import admin
from store.models.item import Item
from store.models.category import Category


class ItemList(admin.ModelAdmin):
    list_display = ['name', 'price', 'category']

    
class CategoryList(admin.ModelAdmin):
    list_display = ['name']

admin.site.register(Item, ItemList)
admin.site.register(Category, CategoryList)
