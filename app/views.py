from django.views.generic import ListView, DetailView, TemplateView
from .models import Child

# Create your views here.

class viewListChildren(ListView):
    model=Child
    template_name = 'home.html'
    context_object_name = 'listChildren'