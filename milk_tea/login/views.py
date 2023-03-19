from django.shortcuts import render, redirect, HttpResponse
from django.urls import reverse_lazy
from django.contrib.auth.views import LoginView, PasswordResetView, PasswordChangeView
from django.contrib import messages
from django.contrib.messages.views import SuccessMessageMixin
from django.views import View
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate
from django.contrib.auth.models import Permission

from .forms import RegisterForm, LoginForm, UpdateUserForm, UpdateProfileForm
from customer.models import KhachHang

def home(request):
    return render(request, 'homepage/index.html')


class RegisterView(View):
    form_class = RegisterForm
    initial = {'key': 'value'}
    template_name = 'homepage/register.html'

    def dispatch(self, request, *args, **kwargs):
        # will redirect to the home page if a user tries to access the register page while logged in
        if request.user.is_authenticated:
            return redirect(to='/')

        # else process dispatch as it otherwise normally would
        return super(RegisterView, self).dispatch(request, *args, **kwargs)

    def get(self, request, *args, **kwargs):
        form = self.form_class(initial=self.initial)
        return render(request, self.template_name, {'form': form})

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)

        if form.is_valid():
            form.save()

            username = form.cleaned_data.get('username')
            lastname = form.cleaned_data.get('last_name')
            firstname = form.cleaned_data.get('first_name')
            email = form.cleaned_data.get('email')
            itemKhachHang = KhachHang(hoKH = firstname, tenKH = lastname, email = email)
            itemKhachHang.save()
            messages.success(request, f'Tài khoản {username} được tạo thành công.')

            return redirect(to='login')

        return render(request, self.template_name, {'form': form})


# Class based view that extends from the built in login view to add a remember me functionality
class CustomLoginView(LoginView):
    form_class = LoginForm

    def form_valid(self, form):
        remember_me = form.cleaned_data.get('remember_me')
        username_in = form.cleaned_data.get('username')
        password_in = form.cleaned_data.get('password')

        if not remember_me:
            # set session expiry to 0 seconds. So it will automatically close the session after the browser is closed.
            self.request.session.set_expiry(0)

            # Set session as modified to force data updates/cookie to be saved.
            self.request.session.modified = True

        user = authenticate(username = username_in, password = password_in)
        if user.is_superuser:
            return super(CustomLoginView, self).form_valid_admin(form)
        if user.is_staff:
            return super(CustomLoginView, self).form_valid_staff(form)

        # user.has_perms(self, user.get_all_permissions())
        # if user is not None:
        #     if user.get_group_permissions(merchant) == merchant:
        # else browser session will be as long as the session cookie time "SESSION_COOKIE_AGE" defined in settings.py

        return super(CustomLoginView, self).form_valid(form)
        # form.cleaned_data.get('username')

class ResetPasswordView(SuccessMessageMixin, PasswordResetView):
    template_name = 'homepage/password_reset.html'
    email_template_name = 'homepage/password_reset_email.html'
    subject_template_name = 'homepage/password_reset_subject'
    success_message = "We've emailed you instructions for setting your password, " \
                      "if an account exists with the email you entered. You should receive them shortly." \
                      " If you don't receive an email, " \
                      "please make sure you've entered the address you registered with, and check your spam folder."
    success_url = reverse_lazy('login-home')


class ChangePasswordView(SuccessMessageMixin, PasswordChangeView):
    template_name = 'homepage/change_password.html'
    success_message = "Successfully Changed Your Password"
    success_url = reverse_lazy('login-home')


# @login_required
# def profile(request):
#     if request.method == 'POST':
#         user_form = UpdateUserForm(request.POST, instance=request.user)
#         profile_form = UpdateProfileForm(request.POST, instance=request.user)


#         if user_form.is_valid() and profile_form.is_valid():

#             user_form.save()
#             profile_form.save()

#             sdt = profile_form.cleaned_data.get('sdt')

#             diaChi = profile_form.cleaned_data.get('diaChi')
#             itemKhachHang = KhachHang.objects.get(email = request.user.email)
#             itemKhachHang.sdt = sdt
#             itemKhachHang.diaChi = diaChi
#             itemKhachHang.save()
#             messages.success(request, 'Your profile is updated successfully')
#             return redirect(to='login')
#     else:
#         user_form = UpdateUserForm(instance=request.user)
#         profile_form = UpdateProfileForm(instance=request.user)

#     return render(request, 'homepage/profile.html', {'user_form': user_form, 'profile_form': profile_form})


@login_required
def profile(request):
    if request.method == 'POST':
        user_form = UpdateUserForm(request.POST, instance=request.user)
        profile_form = UpdateProfileForm(request.POST, instance=request.user)


        if user_form.is_valid() and profile_form.is_valid():

            user_form.save()
            profile_form.save()

            sdt = profile_form.cleaned_data.get('sdt')

            diaChi = profile_form.cleaned_data.get('diaChi')
            itemKhachHang = KhachHang.objects.get(email = request.user.email)
            itemKhachHang.sdt = sdt
            itemKhachHang.diaChi = diaChi
            itemKhachHang.save()
            messages.success(request, 'Cập nhật thông tin thành công')
            return redirect(to='login')
    else:
        user_form = UpdateUserForm(instance=request.user)
        profile_form = UpdateProfileForm(instance=request.user)

    return render(request, 'homepage/profile.html', {'user_form': user_form, 'profile_form': profile_form})