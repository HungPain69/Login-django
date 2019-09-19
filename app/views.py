from django.views.generic import ListView, DetailView, TemplateView
from .models import Item

# Create your views here.


class ListViewItem(ListView):
    model=Item
    template_name = 'home.html'
    context_object_name = 'list_item'