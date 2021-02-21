from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from dashboard.forms import CategoryForm
from store.models import Category


def category_delete(request, pk):
    category = Category.objects.get(id = pk)
    if request.method == 'POST':
        category.delete()
        return redirect('home')
    return render(request, 'dashboard/modals/category_delete.html', {'category':category})

def category_create(request):
    if request.session.get('user_type') == 'seller':
        if request.method == 'GET':
            form = CategoryForm()
        if request.method == 'POST':
            form = CategoryForm(request.POST)
            if form.is_valid():
                form.save()
                return redirect('home')
        return render(request, 'dashboard/modals/category_form.html',{'form': form})

def category_update(request, pk):
    if request.session.get('user_type') == 'seller':
        category = get_object_or_404(Category, pk=pk)
        if request.method == 'GET':
            form = CategoryForm(instance = category)
        if request.method == 'POST':
            form = CategoryForm(request.POST,instance = category)
            if form.is_valid():
                form.save()
                return redirect('home')
        return render(request, 'dashboard/modals/category_form.html',{'form': form})
    else:
        return redirect('home')