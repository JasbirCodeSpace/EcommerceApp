from django import template

register = template.Library()

@register.filter(name='is_cart_empty')
def is_cart_empty(cart):
    if not cart:
        return True
    else:
        return False
        
@register.filter(name='is_item_in_cart')
def is_item_in_cart(item, cart):
    if str(item.id) in cart.keys():
        return True
    else:
        return False

@register.filter(name='item_quantity_in_cart')
def item_quantity_in_cart(item, cart):
    return cart.get(str(item.id))

@register.filter(name='item_total_price')
def item_total_price(item, cart):
    return item.price * item_quantity_in_cart(item, cart)

@register.filter(name='cart_total_price')
def cart_total_price(items, cart):
    total = 0
    for item in items:
        total += item_total_price(item, cart)
    return total
