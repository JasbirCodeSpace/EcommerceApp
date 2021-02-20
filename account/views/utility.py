from django.shortcuts import render, redirect
from django.http import HttpResponse

def logout(request):
    request.session.clear()
    return redirect('home')

def login(request):
    if request.session.get('user_id'):
        return redirect('home')
    else:
        return render(request, 'account/account.html')

def signup(request):
    if request.session.get('user_id'):
        return redirect('home')
    else:
        return render(request, 'account/account.html')
