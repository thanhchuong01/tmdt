"""milk_tea URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include, re_path

from django.conf.urls.static import static
from django.conf import settings

from django.contrib.auth import views as auth_views
from login.views import CustomLoginView, ResetPasswordView, ChangePasswordView
from login.forms import LoginForm

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('core.urls')),
    path('', include('product.urls')),
    path('', include('cart.urls')),
    path('', include('order.urls')),
    path('', include('customer.urls')),
    path('', include('emp.urls')),
    path('', include('login.urls')),

    path(r'^login$', auth_views.LoginView.as_view(template_name='accounts/login.html')),

    path('login/',
       CustomLoginView.as_view(redirect_authenticated_user=True, template_name='homepage/login.html',
                               authentication_form=LoginForm), name='login'),

    path('logout/', auth_views.LogoutView.as_view(template_name='homepage/logout.html'), name='logout'),

    path('password-reset/', ResetPasswordView.as_view(), name='password_reset'),

    path('password-reset-confirm/<uidb64>/<token>/',
       auth_views.PasswordResetConfirmView.as_view(template_name='homepage/password_reset_confirm.html'),
       name='password_reset_confirm'),

    path('password-reset-complete/',
       auth_views.PasswordResetCompleteView.as_view(template_name='homepage/password_reset_complete.html'),
       name='password_reset_complete'),

    path('password-change/', ChangePasswordView.as_view(), name='password_change'),

    re_path(r'^oauth/', include('core.urls')),
    re_path(r'^oauth/', include('product.urls')),

    # path(r'^login$', auth_views.LoginView.as_view(template_name='accounts/login.html')),

    # path('login/',
    #    CustomLoginView.as_view(redirect_authenticated_user=True, template_name='homepage/login.html',
    #                            authentication_form=LoginForm), name='login'),

    # path('logout/', auth_views.LogoutView.as_view(template_name='homepage/logout.html'), name='logout'),

    # path('password-reset/', ResetPasswordView.as_view(), name='password_reset'),

    # path('password-reset-confirm/<uidb64>/<token>/',
    #    auth_views.PasswordResetConfirmView.as_view(template_name='homepage/password_reset_confirm.html'),
    #    name='password_reset_confirm'),

    # path('password-reset-complete/',
    #    auth_views.PasswordResetCompleteView.as_view(template_name='homepage/password_reset_complete.html'),
    #    name='password_reset_complete'),

    # path('password-change/', ChangePasswordView.as_view(), name='password_change'),

    # re_path(r'^oauth/', include('core.urls')),


] + static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
