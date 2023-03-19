from django.urls import path


from .views import Index, search, getContact


urlpatterns = [
    path('', Index.as_view(), name = 'index'), 
    path('search/', search, name='search'),
    path('contact/', getContact, name='contact'),
    
] 
