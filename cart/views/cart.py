from django.shortcuts import render, redirect
from django.http import HttpResponse
from store.models.item import Item
from store.models.category import Category
from django.views import View

class Cart(View):
    def get(self, request):
        cart = request.session.get('cart')
        if cart:
            ids = list(request.session.get('cart').keys())
            items = Item.get_item_by_id(ids)
        else:
            request.session['cart'] = {}
            items = {}
        return render(request, 'cart/cart.html', {'items':items})
    def post(self, request):
        pass