from django.shortcuts import render, redirect
from django.http import HttpResponse
from store.models.item import Item
from store.models.order import Order
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
        items = Item.get_item_by_id(list(cart.keys()))
        for item in items:
            order = Order(customer = Customer.get_customer_by_id(customer_id),
                            item = item,
                            quantity = cart.get(str(item.id)),
                            price = item.price,
                            address = address,
                            city = city,
                            state = state,
                            country = country,
                            zip_code = zip_code)
            
            if order.place_order():
                request.session['cart'] = {}

        return redirect('cart')
    def get(self, request):
        return redirect('cart')