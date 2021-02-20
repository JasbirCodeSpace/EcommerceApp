from django.shortcuts import render, redirect
from django.http import HttpResponse
from account.models.customer import Customer
from store.models.item import Item
from store.models.category import Category
from store.models.order import Order

def statistics(request):
    if request.session.get('user_type') == 'seller':
        categories = Category.get_all_categories()
        orders = Order.get_all_orders()
        items = Item.get_all_items()
        customers = Customer.objects.all()
        category_pie = categories_chart(categories)
        context = {
            'categories': categories,
            'orders': orders,
            'items': items,
            'customers': customers,
            'category_pie': category_pie
        }
        return render(request, 'store/statistics.html', context)
    return redirect('home')

def categories_chart(categories):
    labels = []
    chartLabel = "Products by Categories"
    chartData = []
    for category in categories:
        labels.append(category.name)
        chartData.append(Item.get_items_by_category_id(category.id).count())
    data ={ 
            "labels":labels, 
            "chartLabel":chartLabel, 
            "chartData":chartData, 
             } 
    return data