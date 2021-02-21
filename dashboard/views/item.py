from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from dashboard.forms import ItemForm
from store.models import Item


def item_delete(request, pk):
    item = get_object_or_404(Item, pk = pk)
    if request.method == 'POST':
        item.delete()
        return redirect('home')
    return render(request, 'dashboard/modals/delete_form.html', {'item':item})

def item_create(request):
    if request.session.get('user_type') == 'seller':
        if request.method == 'GET':
            form = ItemForm()
        if request.method == 'POST':
            form = ItemForm(request.POST, request.FILES)
            if form.is_valid():
                form.save()
                return redirect('home')
        return render(request, 'dashboard/modals/item_form.html',{'form': form})

def item_update(request, pk):
    if request.session.get('user_type') == 'seller':
        item = get_object_or_404(Item, pk=pk)
        if request.method == 'GET':
            form = ItemForm(instance = item)
        if request.method == 'POST':
            print(item.id, item.image)
            form = ItemForm(request.POST, request.FILES, instance = item)
            if form.is_valid():
                form.save()
                return redirect('home')
        return render(request, 'dashboard/modals/item_form.html',{'form': form})
    else:
        return redirect('home')