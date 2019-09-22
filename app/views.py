from django.views.generic import ListView, DetailView, TemplateView
from .models import Item, UserProfile
from django.shortcuts import render, get_object_or_404


# Create your views here.
def products(request):
    template = 'a.html'
    context = {
        'items': Item.objects.all()
    }
    return render(request, template , context)


class ListViewItem(ListView):
    model=Item
    template_name = 'home.html'
    paginate_by = 10
    context_object_name = 'list_item'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['pain'] = Item.objects.values('category').distinct()
        return context


class ItemDetailView(DetailView):
    module = Item
    template_name = 'product.html'
    queryset = Item.objects.all()