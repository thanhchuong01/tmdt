from django.shortcuts import render,redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required

from order.models import DonHang, CTDonHang
from customer.models import KhachHang

# Create your views here.

@login_required
def getViewCustomer(request):
    return render(request, "homepage/customer/customer.html")

@login_required
def index(request):

    if request.user.is_anonymous:
        messages.warning(request, f"Bạn cần phải đăng nhập để tiếp tục!")
        return redirect('/login')

    email =request.user.email
    kh= KhachHang.objects.get(email= email)

    dhOfKh = DonHang.objects.filter(maKH = kh)


    context = {
        'listdh' : dhOfKh,
    }
    return render(request, 'homepage/customer/customer.html', context)

@login_required
def cancel_dh(request, int):

    if DonHang.objects.filter(maDH = int).exists():

        dh_cancel = DonHang.objects.get(maDH = int)
        print(dh_cancel)
        dh_cancel.delete()
        messages.success(request,  f"Xóa đơn hàng thành công.")


    return redirect('index')
