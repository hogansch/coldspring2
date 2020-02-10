from django import template
from datetime import timedelta

register = template.Library()

@register.filter(name="add_day")
def add_day(value):
    return value + timedelta(days=1)

