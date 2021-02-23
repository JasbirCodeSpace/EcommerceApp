from django.shortcuts import render, redirect
from django.http import HttpResponse
from store.models.item import Item
from orders.models.order import Order
from orders.models.order_item import OrderItem
from account.models.customer import Customer
from django.views import View

class CheckOut(View):
    def post(self, request):
        address = request.POST.get('address')
        city = request.POST.get('city')
        state = request.POST.get('state')
        country = request.POST.get('country')
        zip_code= request.POST.get('zip')
        customer_id = request.session.get('user_id')

        cart = request.session.get('cart')
        items = self.get_items(cart)
        order = Order(customer = Customer.get_customer_by_id(customer_id),
                        total_price = self.get_total_price(cart, items),
                        status = False,
                        address = address,
                        city = city,
                        state = state,
                        country = country,
                        zip_code = zip_code
                    )
        if order.place_order():
            for item in items:
                order_item = OrderItem(order = order,
                                                item = item,
                                                quantity = self.get_quantity(cart, item),
                                                price = item.price)
                order_item.save()
            request.session['cart'] = {}

        return redirect('cart')
    def get(self, request):
        return redirect('cart')
    
    def get_total_price(self, cart, items):
        price = 0
        for item in items:
            price += item.price*cart.get(str(item.id))
        return price

    def get_items(self,cart):
        return Item.get_item_by_id(list(cart.keys()))

    def get_quantity(self, cart, item):
        return cart.get(str(item.id))
    
