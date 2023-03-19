from django.urls import path

from .views import getAllProduct, getDMProduct, getDetailProduct, addReview


# app_name= 'product'

urlpatterns = [
    path('product', getAllProduct, name = 'allmon'), 
    path('product/<mon_id>/', getDetailProduct, name = 'detailmon'), 
    path('category/<id>', getDMProduct, name = 'DMmon'), 
    path('reviews', addReview, name = 'addReview'),
    
]
