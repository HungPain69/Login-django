from django.urls import path,include
from .views import  ListViewItem, ItemDetailView, products
from . import  views

urlpatterns = [
    path('', ListViewItem.as_view(), name ='home'),
    path('product/<slug>',ItemDetailView.as_view(), name = 'product'),


]
