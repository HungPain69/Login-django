from django.views.generic import ListView, DetailView, TemplateView
from .models import Item

# Create your views here.
def products(request):
    context = {
        'items': Item.objects.all()
    }
    return render(request, "products.html", context)

class ListViewItem(ListView):
    model=Item
    template_name = 'home.html'
    paginate_by = 1
    context_object_name = 'list_item'

    def get_queryset(self):
        return Item.objects.all()

class ItemDetailView(DetailView):
    module = Item
    template_name = 'product.html'
    queryset = Item.objects.all()