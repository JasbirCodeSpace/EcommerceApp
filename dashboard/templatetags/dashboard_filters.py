from django import template
from babel.numbers import format_currency
register = template.Library()

@register.filter(name = 'currency')
def currency(price):
    return format_currency(price, 'INR', locale='en_IN')

@register.filter(name='mul')
def mul(a, b):
    return a*b

@register.filter(name='is_seller')
def is_seller(request):
    if request.session.get('user_id'):
        if request.session.get('user_type')=="seller":
            return True
    return False

@register.filter(name='is_customer')
def is_customer(request):
    if request.session.get('user_id'):
        if request.session.get('user_type')=="customer":
            return True
    return False


