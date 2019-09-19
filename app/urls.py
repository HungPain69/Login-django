from django.urls import path,include
from .views import ListViewItem

urlpatterns = [
    path('', ListViewItem.as_view(), name ='home'),
    

]
