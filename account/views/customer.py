from django.shortcuts import render, redirect
from django.http import HttpResponse
from account.models.customer import Customer
from account.forms import CustomerForm, CustomerLoginForm
from django.contrib import messages
from django.contrib.auth.hashers import make_password, check_password
from django.views import View

class CustomerSignup(View):
    def get(self, request):
        if request.session.get('user_id'):
            return redirect('home')
        
        form = CustomerForm()
        return render(request, 'account/signup.html', {'form': form})
    
    def post(self, request):
        if request.session.get('user_id'):
            return redirect('home')
        form = CustomerForm(request.POST)
        if form.is_valid():
            customer = form.save(commit=False)
            customer.password = make_password(customer.password)
            customer.save()
            messages.success(request, f'Account Created')
            return redirect('customer-login')
        return render(request, 'account/signup.html', {'form': form})

class CustomerLogin(View):
    def get(self, request):
        if request.session.get('user_id'):
            return redirect('home')
        form = CustomerLoginForm()
        return render(request, 'account/login.html', {'form':form})

    def post(self, request):
        if request.session.get('user_id'):
            return redirect('home')
        error_message = None
        form = CustomerLoginForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data.get('email')
            password = form.cleaned_data.get('password')
            customer = Customer.get_customer_by_email(email)
            if customer:
                if check_password(password, customer.password):
                    request.session['user_id'] = customer.id
                    request.session['user_type'] = 'customer'
                    return redirect('home')
                else:
                    error_message = "Incorrect password"
            else:
                error_message = "Invalid email or password"
            return render(request, 'account/login.html', {'form':form, 'error':error_message})