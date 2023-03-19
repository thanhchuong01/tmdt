from django.urls import path
from .views import home, profile, RegisterView

urlpatterns = [
    path('loginhome/', home, name='login-home'),
    path('register/', RegisterView.as_view(), name='users-register'),
    path('accounts/profile/', profile, name='users-profile'),
]
