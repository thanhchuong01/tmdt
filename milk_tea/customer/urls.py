from django.urls import path

from .views import getViewCustomer, index, cancel_dh


# app_name= 'product'

urlpatterns = [
    # path('customer/', getViewCustomer, name = 'customerview'), 
    path('customer/', index, name='customerview'),
    path('huydh/<int>', cancel_dh, name='cancel_dh'),
    
    
]
