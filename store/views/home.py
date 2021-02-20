from django.shortcuts import render, redirect
from django.http import HttpResponse
from store.models.item import Item
from store.models.category import Category
from django.views import View

class Index(View):
    def get(self, request):
        if request.session.get('user_type')=='seller':
            return self.seller_get(request)
        else:
            return self.customer_get(request)
    
    def post(self, request):
        if request.session.get('user_type') == 'seller':
            return self.seller_post(request)
        else:
            return self.customer_post(request)

    def customer_get(self, request):
        cart = request.session.get('cart')
        if not cart:
            request.session['cart'] = {}
        categories = Category.get_all_categories()
        category_id = request.GET.get('category')
        query = request.GET.get('q')
        items = None
        if query:
            items = Item.get_items_by_query(query)
        elif category_id:
            items = Item.get_items_by_category_id(category_id)
        else:
            items = Item.get_all_items()
        return render(request, 'store/customer.html', {'items': items, 'categories': categories})

    def seller_get(self, request):
        items = Item.get_all_items()
        categories = Category.get_all_categories()
        return render(request, 'store/seller.html', {'items':items, 'categories':categories})
    def customer_post(self, request):
        item = request.POST.get('item')
        remove = request.POST.get('remove')
        cart = request.session.get('cart')
        if cart:
            if item in cart.keys() and remove:
                if remove == 'False':
                    cart[item] += 1
                else:
                    if cart[item]<=1:
                        cart.pop(item)
                    else:
                        cart[item] -= 1
            else:
                cart[item] = 1
        else:
            cart = {}
            cart[item] = 1
        request.session['cart'] = cart
        return redirect('home')

    def seller_post(self, request):
        pass

