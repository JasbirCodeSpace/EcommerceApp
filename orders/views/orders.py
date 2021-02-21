from django.shortcuts import render, redirect
from django.http import HttpResponse
from account.models.customer import Customer
from store.models.item import Item
from store.models.category import Category
from orders.models.order import Order
from django.views import View

class Orders(View):
    def get(self, request):
        if request.session.get('user_type') == 'seller':
            orders = Order.get_all_orders()
            return render(request, 'orders/seller.html', {'orders':orders})
        else:
            customer_id = request.session.get('user_id')
            orders = Order.get_orders_by_customer_id(customer_id)
            return render(request, 'orders/customer.html', {'orders': orders})
    def post(self, request):
        pass