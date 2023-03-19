from django.urls import path

from .views import cart_view, add_to_cart, removeCart, upQuantity, downQuantity


# app_name= 'product'

urlpatterns = [
    path('cart/<mon_id>/', add_to_cart, name = 'addcart'), 
    path('cart/', cart_view, name = 'cart_view'),
    path('cart/remove-cart/<cart_id>', removeCart, name = 'delcart'),
    path('cart/up/<cart_id>', upQuantity, name = 'upquantity'),
    path('cart/down/<cart_id>', downQuantity, name = 'downquantity'),  
    
    
]
