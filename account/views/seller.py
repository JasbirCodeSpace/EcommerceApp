from django.shortcuts import render, redirect
from django.http import HttpResponse
from account.models.seller import Seller
from account.forms import SellerForm, SellerLoginForm
from django.contrib import messages
from django.contrib.auth.hashers import make_password, check_password
from django.views import View


class SellerSignup(View):
    def get(self, request):
        if request.session.get('user_id'):
            return redirect('home')
        form = SellerForm()
        return render(request, 'account/signup.html', {'form': form})

    def post(self, request):
        if request.session.get('user_id'):
            return redirect('home')
        form = SellerForm(request.POST)
        if form.is_valid():
            seller = form.save(commit=False)
            seller.password = make_password(seller.password)
            seller.save()
            messages.success(request, f'Account Created')
            return redirect('seller-login')
        return render(request, 'account/signup.html', {'form': form})


class SellerLogin(View):
    def get(self, request):
        if request.session.get('user_id'):
            return redirect('home')
        form = SellerLoginForm()
        return render(request, 'account/login.html', {'form':form})

    def post(self, request):
        if request.session.get('user_id'):
            return redirect('home')
        error_message = None
        form = SellerLoginForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data.get('email')
            password = form.cleaned_data.get('password')
            seller = Seller.get_seller_by_email(email)
            if seller:
                if check_password(password, seller.password):
                    request.session['user_id'] = seller.id
                    request.session['user_type'] = 'seller'
                    request.session['user_name'] = seller.first_name +" "+ seller.last_name
                    return redirect('home')
                else:
                    error_message = "Incorrect password"
            else:
                error_message = "Invalid email or password"
            return render(request, 'account/login.html', {'form':form, 'error':error_message})