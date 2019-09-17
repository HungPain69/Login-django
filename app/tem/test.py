from django import template
from app.models import Child

register = template.Library()

@register.filter
def cart(user):
    pass