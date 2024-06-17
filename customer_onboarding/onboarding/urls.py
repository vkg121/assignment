from django.urls import path
from . views import *

urlpatterns = [
    path('create/', create_customer, name='create_customer'),
    path('list/', list_customers, name='list_customers'),
]


