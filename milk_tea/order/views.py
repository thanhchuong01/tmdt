from django.shortcuts import render,redirect, get_object_or_404
from django.views import View
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.utils.http import urlencode
from django.urls import reverse
from django.contrib.auth.decorators import login_required

from .models import DonHang, CTDonHang, KhuyenMai,ThanhToan
from cart.models import GioHang, CTGioHang
from customer.models import KhachHang

import datetime
from decimal import Decimal


# Create your views here.

@login_required
def getDonHang(request):

    today= datetime.date.today()

    if request.user.is_anonymous:
        messages.warning(request, f"Bạn cần phải đăng nhập để tiếp tục!")
        return redirect('/login')

    email =request.user.email
    kh= KhachHang.objects.get(email= email)
    khachhang= KhachHang.objects.filter(email= email)
    print("khach: ",khachhang)
    giohang, created= GioHang.objects.get_or_create(maKH = kh, trangThai= True)

    # kh = KhachHang.objects.get(maKH= 1)
    # giohang, created = GioHang.objects.get_or_create(maKH= kh, trangThai = True) # request.user
    ct_giohang = CTGioHang.objects.filter(maGH=giohang)
    thanhtoan= ThanhToan.objects.all()

    ship = 30
    total = sum(item.soLuong * item.giaMon for item in ct_giohang) + ship
    # print('total1:',    total)

    context={
        'cart_items': ct_giohang,
        'total':total, 
        'ship':ship,
        'payment':thanhtoan,
        'khachhang':khachhang

    }

    coupon= request.GET.get('cp')
    # print("cp",coupon)

    cp= KhuyenMai.objects.filter(code= coupon, trangThai= True, ngayHetHan__gte = today).values_list('phantramKM', flat=True)
    # print("cp2:", cp)
    if coupon:
        makm= KhuyenMai.objects.get(code= coupon, trangThai= True, ngayHetHan__gte = today)
    # print("maKM:", maKM[0])
    # if makm:
    #     maKM=makm[0]
    # print(maKM)

    discount=0

    if cp:
        sotiengiam= round((Decimal(sum(cp)) / 100)*total)
        # print('giam:',sotiengiam)
        total_discount = total - sotiengiam 
        # print('tong:', total_discount)
        context['total_discount']= total_discount
        discount= total_discount

    # print("discount: ",discount)

    if request.method == 'POST':
        ho = request.POST.get('ho')
        ten = request.POST.get('ten')
        sdt = request.POST.get('sdt')
        diachi = request.POST.get('diachi')
        xaphuong = request.POST.get('xaphuong')
        quanhuyen = request.POST.get('quanhuyen')
        tinhtp = request.POST.get('tinhtp')
        pay = request.POST.get('payment')
        # print(pay)
        
        

        if ho == '':
            messages.warning(request,  f"Họ không được để trống.")
            return redirect('bill')
        if ten == '':
            messages.warning(request,  f"Tên không được để trống.")
            return redirect('bill')
        if sdt == '':
            messages.warning(request,  f"Số điện thoại không được để trống.")
            return redirect('bill')
        if diachi == '':
            messages.warning(request,  f"Địa chỉ không được để trống.")
            return redirect('bill')
        if xaphuong == '':
            messages.warning(request,  f"Xã phườngkhông được để trống.")
            return redirect('bill')
        if quanhuyen == '':
            messages.warning(request,  f"Quận huyện không được để trống.")
            return redirect('bill')
        if tinhtp == '':
            messages.warning(request,  f"Tỉnh thành phố không được để trống.")
            return redirect('bill')
        
        if pay == None:
            messages.warning(request,  f"Vui lòng chọn phương thức thanh toán.")
            return redirect('bill')
            
        else:
            payid= ThanhToan.objects.get(maTT=pay)
            print(payid)

        hoten= ho+ten
        # print(hoten)
        diachigiao = diachi + ", " +xaphuong+ ", " + quanhuyen+ ", " + tinhtp
        print("diachigiao: ",diachigiao)

        if cp:
            if payid.maTT == 2: #momo
                DonHang.objects.create(maKH= kh, tongTien=discount,maKM=makm,maTT=payid, diachi=diachigiao,sdt= sdt, hoten=hoten )
                KhuyenMai.objects.filter(code= coupon).update(trangThai= False)
                GioHang.objects.filter(maKH= kh).update(trangThai=False)
                return redirect('momo',a.maDH)

            else:
                a=DonHang.objects.create(maKH= kh, tongTien=discount,maKM=makm,maTT=payid, diachi=diachigiao,sdt= sdt, hoten=hoten )
                KhuyenMai.objects.filter(code= coupon).update(trangThai= False)
                GioHang.objects.filter(maKH= kh).update(trangThai=False)
                # print("aaaaaaaaaaaa:", a.maDH)
                return redirect('customerview')
        else:
            if payid.maTT == 2: #momo 
                b=DonHang.objects.create(maKH= kh, tongTien=total,maTT=payid, diachi=diachigiao,sdt= sdt, hoten=hoten )
                GioHang.objects.filter(maKH= kh).update(trangThai=False)
                return redirect('momo',b.maDH)

            else:
                DonHang.objects.create(maKH= kh, tongTien=total,maTT=payid, diachi=diachigiao,sdt= sdt, hoten=hoten )
                GioHang.objects.filter(maKH= kh).update(trangThai=False)
                return redirect('customerview')

    
        
    return render(request, 'homepage/order/checkout.html', context)


@login_required
def getDiscount(request):

    today= datetime.date.today()

    if request.user.is_anonymous:
        messages.warning(request, f"Bạn cần phải đăng nhập để tiếp tục!")
        return redirect('/login')

    email =request.user.email
    kh= KhachHang.objects.get(email= email)
    giohang, created= GioHang.objects.get_or_create(maKH = kh, trangThai= True)

    # kh = KhachHang.objects.get(maKH= 1)
    # giohang, created = GioHang.objects.get_or_create(maKH= kh, trangThai = True) # request.user
    ct_giohang = CTGioHang.objects.filter(maGH=giohang)

    ship = 30
    total = sum(item.soLuong * item.giaMon for item in ct_giohang) + ship
    # print('total1:',    total)

    if request.method == 'POST':
        coupon= request.POST.get('coupon')
        # print(coupon)

        cp= KhuyenMai.objects.filter(code= coupon, trangThai= True, ngayHetHan__gte = today).values_list('phantramKM', flat=True)
        
        if cp:
            sotiengiam= round((Decimal(sum(cp)) / 100)*total)
            # print('giam:',sotiengiam)
            total_discount = total - sotiengiam +ship
            # print('tong:', total_discount)
            # price_discount= total_discount
            # KhuyenMai.objects.filter(code= coupon).update(trangThai= False)
            messages.success(request,  f"Sử dụng mã thành công.")
            return redirect(reverse('bill') + '?' + urlencode({'cp': coupon }))
        else:
            messages.warning(request,  f"Mã giảm giá không tồn tại hoặc đã hết hạn.")
            return redirect('bill')
    return redirect('bill')

@login_required
def checkMOMO(request, id_dh):

    # donhang= DonHang.objects.filter(maDH= id_dh)
    donhang= get_object_or_404(DonHang, pk= id_dh)

    context={
        'dh': donhang
    }

    return render(request, 'homepage/order/momo.html', context)
