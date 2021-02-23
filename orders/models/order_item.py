from django.db import models
from account.models import Customer
from store.models.item import Item
from orders.models.order import Order

class OrderItem(models.Model):
    order = models.ForeignKey(Order, on_delete = models.CASCADE, related_name='order_item')
    item = models.ForeignKey(Item, on_delete = models.CASCADE)
    quantity = models.IntegerField(default=1)
    price = models.FloatField()

    @staticmethod
    def get_orders_by_order(order):
        return OrderDescription.objects.filter(order = order)