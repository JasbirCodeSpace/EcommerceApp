from django.db import models
from account.models import Customer
from store.models.item import Item

class Order(models.Model):
    item = models.ForeignKey(Item, on_delete=models.CASCADE)
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    quantity = models.IntegerField(default=1)
    price = models.FloatField()
    date = models.DateTimeField(auto_now_add=True)
    status = models.BooleanField(default=False)
    address = models.CharField(
        "Address",
        max_length=1024,
    )

    zip_code = models.CharField(
        "ZIP / Postal code",
        max_length=12,
    )

    city = models.CharField(
        "City",
        max_length=1024,
    )

    state = models.CharField(
        "State",
        max_length=1024
    )

    country = models.CharField(
        "Country",
        max_length=1024,
    )

    def place_order(self):
        self.save()
        return True

    @staticmethod
    def get_orders_by_customer_id(customer_id):
        if Customer.get_customer_by_id(customer_id):
            return Order.objects.filter(customer = customer_id).order_by('-date')
    
    @staticmethod
    def get_all_orders():
        return Order.objects.all()