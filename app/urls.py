from django.urls import path,include
from .views import viewListChildren

urlpatterns = [
    path('',viewListChildren.as_view(), name ='home'),
    

]
