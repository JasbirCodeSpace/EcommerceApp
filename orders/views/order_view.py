from django.shortcuts import render, redirect
from django.http import HttpResponse
from account.models.customer import Customer
from store.models.item import Item
from store.models.category import Category
from orders.models.order import Order
from orders.models.order_item import OrderItem
from django.views import View

class OrderAction(View):
    def get(self, request):
        customer_id = request.session.get('user_id')
        if customer_id:
            order_id = request.GET['id']
            if request.session.get('user_type')=='customer':
                orders = Order.get_orders_by_customer_id(customer_id)
                order = orders.filter(pk = order_id).first()
            else:
                order = Order.objects.filter(pk = order_id).first()
            if order:
                return render(request, 'orders/order.html', {'order': order})
            
        return render(request, 'orders/order.html', {'order': {}})
    def post(self, request):
        pass