from django import template
from babel.numbers import format_number


register = template.Library()

@register.filter(name='count')
def count(obj):
    return format_number(obj.count(), locale='en_IN')
