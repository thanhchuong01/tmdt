from django.urls import path

from .views import getDonHang, checkMOMO,getDiscount


# app_name= 'product'

urlpatterns = [
    path('checkout/', getDonHang, name = 'bill'),  
    path('checkout/coupon/', getDiscount, name = 'coupon'),  
    path('checkout/momo/<id_dh>', checkMOMO, name = 'momo'),
   
    
    
]
