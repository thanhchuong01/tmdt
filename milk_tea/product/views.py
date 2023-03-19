from django.shortcuts import render,redirect, get_object_or_404
from django.views import View
from django.contrib import messages
from django.db.models import Avg

from product.models import Danhmuc, Mon, CTGia, CTDanhGia
from cart.models import GioHang, CTGioHang,CTGia
from customer.models import KhachHang
from order.models import CTDonHang, DonHang
from .forms import danhGiaForm



def getAllProduct(request):
    context={
        'dm': Danhmuc.objects.all(),
        'mon': Mon.objects.filter(trangThaiMon=True),
        'count_All': Mon.objects.all().count()
    }

    return render(request, 'homepage/product/menu.html', context)


def getDMProduct(request, id):

    context={
        'dm': Danhmuc.objects.all(),
        'mon': Mon.objects.filter(trangThaiMon=True, maDM= id)
        
    }

    return render(request, 'homepage/product/menu.html', context)



def getDetailProduct(request,mon_id):

    # giamon= Mon.objects.filter(maMon= mon_id).values_list('gia', flat=True)
    # giasize= CTGia.objects.filter(maDM= dm_id).values_list('giaSize', flat=True)

    # total = sum(giamon) + sum(giasize)
    
    # mon = Mon.objects.get(trangThaiMon=True, maMon= mon_id)
    mon= get_object_or_404(Mon, pk= mon_id)
   
    m= get_object_or_404(CTGia ,pk= 1)
    l= get_object_or_404(CTGia ,pk= 2)
    

    mon.sizeMon.add(m)
    mon.sizeMon.add(l)

    sizes= mon.sizeMon.all()

    danhgiaMon = CTDanhGia.objects.filter(maMon = mon_id)
    # print(type(danhgiaMon[0]))
    countdg = CTDanhGia.objects.filter(maMon = mon_id).count
    form = danhGiaForm()

    if request.user.is_anonymous:
        messages.warning(request, f"Bạn cần phải đăng nhập để tiếp tục!")
        return redirect('/login')

    email =request.user.email
    makh= KhachHang.objects.get(email= email)
    print("--------------------------------------------------------- ")
    print("ma khách hàng: ", makh)
    makhachhang= makh.maKH
    print("makhach", makhachhang)
    giohang, created= GioHang.objects.get_or_create(maKH = makh, trangThai= True)

    countcart=0
    # if gh == None:
    #     giohang= GioHang.objects.create(maKH=makh)
    count_cart= CTGioHang.objects.filter(maGH=giohang).count()
    countcart= count_cart
    

    totalrate= CTDanhGia.objects.filter(maMon = mon_id).aggregate(Avg('rating'))['rating__avg']
    print("total rate: ",totalrate)

    context={
        'mon': mon,
        'sizes':sizes,
        'danhgia': danhgiaMon,
        'countdg':countdg,
        'totalrate':totalrate,
        'form' : form,
        'count_cart':countcart,
        'makh':makhachhang

    }

    if request.GET.get('size'):
        size= request.GET.get('size')
        # print(size)
        price= mon.get_product_price_by_size(mon_id,size)
        context['selected_size'] = size
        context['updated_price'] = price
        # print(price)
   
    return render(request, 'homepage/product/detailProduct.html', context)


def addReview(request):
    url = request.META.get('HTTP_REFERER')

    if request.user.is_anonymous:
        messages.warning(request, f"Bạn cần phải đăng nhập để tiếp tục!")
        return redirect('/login')

    # user = request.user.id
    kh = KhachHang.objects.filter(email= request.user.email).values_list('maKH', flat=True)

    user = KhachHang.objects.get(email = request.user.email).maKH

    listdh = list(GioHang.objects.filter(maKH = user, trangThai = False).values_list('maGH', flat=True))
    listmon = list(CTGioHang.objects.filter(maGH__in = listdh).values_list('maMon', flat=True).distinct())

    print(listdh)
    print(listmon)

    if request.method == "POST":
        input = danhGiaForm(request.POST, request.FILES)
        input.is_valid()
        print(input.cleaned_data.get('maMon'))
        if input.cleaned_data.get('maMon') not in listmon or listmon is not None:
            messages.warning(request, f"Bạn không được đánh giá khi chưa mua sản phẩm này")
            return redirect(url)

        input.save()

        messages.success(request, f"Cảm ơn bạn đã đánh giá.")
        return redirect(url)
    return redirect('allmon')
