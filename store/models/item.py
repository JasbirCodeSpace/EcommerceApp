from django.db import models
from .category import Category

class Item(models.Model):
    name = models.CharField(max_length=100)
    price = models.FloatField()
    quantity = models.IntegerField(default=0)
    description = models.TextField(default='' , null=True , blank=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='uploads/products/')

    def __str__(self):
        return self.name

    @staticmethod
    def get_all_items():
        return Item.objects.all()
    
    @staticmethod
    def get_items_by_category_id(category_id):
        if category_id:
            return Item.objects.filter(category = category_id)
        else:
            return get_all_items()
    @staticmethod
    def get_item_by_id(ids):
        return Item.objects.filter(id__in = ids)

    @staticmethod
    def get_items_by_query(query):
        return Item.objects.filter(name__icontains=query)

