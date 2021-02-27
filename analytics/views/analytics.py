from django.shortcuts import render, redirect
from django.http import HttpResponse
from account.models.customer import Customer
from store.models.item import Item
from store.models.category import Category
from orders.models.order import Order
from django.db.models import Count
import json
from django.core.serializers.json import DjangoJSONEncoder

def analytics(request):
    if request.session.get('user_type') == 'seller':
        categories = Category.get_all_categories()
        orders = Order.get_all_orders()
        items = Item.get_all_items()
        customers = Customer.objects.all()
        category_pie = categories_chart(categories)
        orders_pie = orders_chart(orders)
        orders_bar = orders_trend_chart(orders)
        context = {
            'categories': categories,
            'orders': orders,
            'items': items,
            'customers': customers,
            'category_pie': category_pie,
            'orders_pie': orders_pie,
            'orders_bar': orders_bar
        }
        return render(request, 'analytics/seller.html', context)
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

def orders_chart(orders):
    labels = ["Complete", "Pending"]
    chartLabel = "Orders status ratio"
    success = orders.filter(status=True).count()
    pending = orders.filter(status=False).count()
    chartData = [success, pending]
    data = {
        "labels": labels,
        "chartLabel": chartLabel,
        "chartData": chartData
    }
    return data

def orders_trend_chart(orders):
    result = orders.extra({'x' : "date(date)"}).values('x').annotate(y=Count('id'))
    chartData = []
    labels = []
    chartLabel = "Orders per day"
    for data in result:
        labels.append(str(data.get('x')))
        chartData.append(data.get('y'))
    data = {
        "labels": labels,
        "chartLabel": chartLabel,
        "chartData": chartData,
        "count": len(result),
        "dict": json.dumps(list(result), cls=DjangoJSONEncoder)
    }
    return data