from django.shortcuts import render
from django.views import View
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
# Create your views here.

from product.models import Danhmuc, Mon
from cart.models import GioHang, CTGioHang
from customer.models import KhachHang


class Index(View):
    def get(self, request):

        # if request.user.is_anonymous:
        #     # print("m cần login")
        #     messages.warning(request, f"Bạn cần phải đăng nhập để tiếp tục!")
        #     return redirect('/login')

        # email =request.user.email
        # kh= KhachHang.objects.filter(email= email).values_list('maKH', flat=True)
        # makh=sum(kh)
        # giohang= GioHang.objects.get(maKH = makh, trangThai= True)
        # print("gio hang: ", giohang)

        # giohang= GioHang.objects.get(maKH = kh, trangThai= True) # request.user
        # if giohang:
        #     count_cart= CTGioHang.objects.filter(maGH=giohang).count()
        # print(count_cart)
        
        context={
            'dm': Danhmuc.objects.all(),
            'mon': Mon.objects.filter(trangThaiMon=True)
            
        }


        return render(request, 'homepage/index.html', context)


def getTopBar(request):

    if request.user.is_anonymous:
        messages.warning(request, f"Bạn cần phải đăng nhập để tiếp tục!")
        return redirect('/login')

    email =request.user.email
    kh= KhachHang.objects.filter(email= email).values_list('maKH', flat=True)
    makh=sum(kh)
    giohang= GioHang.objects.get(maKH = makh, trangThai= True)
    # kh = KhachHang.objects.get(email= email)
    # print("khach: ",kh)
    # giohang= GioHang.objects.get(maKH = kh, trangThai= True)
    # print("gio hang: ", giohang) # request.user
    if giohang:
        count_cart= CTGioHang.objects.filter(maGH=giohang).count()
    print(count_cart)

    context={
        'dm': Danhmuc.objects.all(),
        'mon': Mon.objects.filter(trangThaiMon=True),
        'count_cart':count_cart
        
    }

    return render(request, 'homepage/topbar.html', context)


def search(request):
    url = request.META.get('HTTP_REFERER')

    key = request.GET.get("value_search")
    if key is None:
        return redirect('allmon')

    result = Mon.objects.filter(tenMon__search = key)

    print(result)

    list_search=[]
    for i in result:
        # print(i)
        b= Mon.objects.get(tenMon=i) 
        # print("bbbbbbbbbb", b.maMon)
        # maM= b.maMon
        # a= Mon.objects.filter(maMon=maM)
        # print("aaaaaaaaaaaa", a)
        list_search.append(b)

    print("list search: ", list_search)

    context= {
        'dm': Danhmuc.objects.all(),
        'listsearch': list_search
    }

    # if request.method == "POST":
    #     search= request.POST.get('value_search')
    #     print("aaaa: ", search)

        
    #     # mon= Mon.objects.get(trangThaiMon=True, tenMon= search)
    #     mon= Mon.objects.filter(trangThaiMon=True, tenMon= search).values_list('maMon', flat=True)

    #     print("món: ", sum(mon))

    #     idmon= sum(mon)
    #     # print(idmon)

    #     if mon:
    #         return redirect('detailmon', idmon)

    # return redirect('allmon')
    return render(request, 'homepage/product/search.html', context)



def getContact(request):
    return render(request, 'homepage/contact.html')
