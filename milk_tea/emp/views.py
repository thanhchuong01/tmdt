from django.shortcuts import render, HttpResponse, redirect, HttpResponseRedirect
# from qly_dh.models import DonHang
from django.contrib import messages
from django.contrib.auth.decorators import login_required

from datetime import date, datetime
from django.utils import timezone
from order.models import DonHang
from .forms import DateForm

# Create your views here.


def index(request):
    # list = DonHang.objects.exclude(trangThaiDH = '5')
    list = DonHang.objects.all()


    context = {
        'list' : list,
    }

    return render(request, "homepage/base/index.html", context)


def view(request):

    if request.user.is_anonymous:
        messages.warning(request, f"Bạn cần phải đăng nhập để tiếp tục!")
        return redirect('/login')

    user = request.user
    if user.is_staff:
        print('aaaaaaaaaaaaaaaa')
    print("tài khoản: ", request.user)

    # today_min = datetime.combine(timezone.now().date(), datetime.today().time().min)
    # today_max = datetime.combine(timezone.now().date(), datetime.today().time().max)

    # objetcs_for_today = MyModel.objects.filter(date__range=(today_min, today_max))

    list_all = DonHang.objects.all()
    print("list: ",list_all)
    # print(today_max)
    # print(today_min)
    # print(timezone.now())
    # print(day)
    context = {
        'list_donhang' : list_all,
        'user': user,
    }

    for item in list_all:
        item.ngayLap = item.ngayLap.strftime('%Y/%m/%d, %H:%M:%S')
        item.tongTien = '{:,}'.format(item.tongTien)


    return render(request, "homepage/base/tables_handle_dh.html", context)

# ==================================
# xử lý trạng thái đơn hàng
# ===================================


def delete_dh(request, input_id):  # 1 xóa đơn hàng
    if DonHang.objects.filter(maDH=input_id).exists():
        dh = DonHang.objects.get(maDH=input_id)
        dh.trangThaiDH = '0'
        dh.save()
        return HttpResponseRedirect('/nhanvien/xuly/')
    else:
        return HttpResponse("Lỗi")


def accept_dh(request, input_id):   # 2 xác nhận đơn hàng
    if DonHang.objects.filter(maDH=input_id).exists():
        dh = DonHang.objects.get(maDH=input_id)
        dh.trangThaiDH = '2'
        dh.save()
        return redirect('/nhanvien/xuly/')
    else:
        return HttpResponse("Lỗi")


def process_dh(request, input_id):  # 3 chế biến đơn hàng
    if DonHang.objects.filter(maDH=input_id).exists():
        dh = DonHang.objects.get(maDH=input_id)
        dh.trangThaiDH = '3'
        dh.save()
        return redirect('/nhanvien/xuly/')
    else:
        return HttpResponse("Lỗi")


def transport_dh(request, input_id):  # 4 vận chuyển đơn hàng
    if DonHang.objects.filter(maDH=input_id).exists():
        dh = DonHang.objects.get(maDH=input_id)
        dh.trangThaiDH = '4'
        dh.save()
        return redirect('/nhanvien/xuly/')
    else:
        return HttpResponse("Lỗi")


def done_dh(request, input_id):  #  5 hoàn thành đơn hàng
    if DonHang.objects.filter(maDH=input_id).exists():
        dh = DonHang.objects.get(maDH=input_id)
        dh.trangThaiDH = '5'
        dh.save()
        return redirect('/nhanvien/xuly/')
    else:
        return HttpResponse("Lỗi")

''' 
========================================
    Thống kê
========================================   
''' 


def statistic(request):

    # if request.user.is_anonymous:
    #     messages.warning(request, f"Bạn cần phải đăng nhập để tiếp tục!")
    #     return redirect('/login')

    list_all = DonHang.objects.filter(trangThaiDH = '5')

    for item in list_all:
        item.ngayLap = item.ngayLap.strftime('%Y/%m/%d, %H:%M:%S')
        item.tongTien = '{:,}'.format(item.tongTien)

    context = {
        'list_donhang' : list_all,
        'form': DateForm,
    }

    return render(request, "homepage/base/tables_views.html", context)


def view_time(request):
    if request.method == "POST":
        data = DateForm(request.POST)
        type_ana = data['type_ana'].value()
        type_view = data['type_ana']
        date_begin = datetime.strptime(data['date_begin'].value(), '%Y-%m-%d').date()
        date_end = datetime.strptime(data['date_end'].value(), '%Y-%m-%d').date()

        form = DateForm(initial={'date_begin': date_begin, 'date_end' : date_end, 'type_ana': type_ana})

        # check input range date
        if date_begin > date_end:
            return HttpResponse("Ngày bắt đầu và kết thúc khong hợp lệ")
        

        # print("aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa")

        result_query = DonHang.objects.filter(ngayLap__gte=date_begin, ngayLap__lte=date_end).order_by('ngayLap')
        print("result1: ",result_query)
        result_query = result_query.filter(trangThaiDH='5')
        print("result2: ",result_query)
        result_query = result_query.values('ngayLap', 'tongTien')
        print("result3: ",result_query)

        list_view = {}

        # thống kê theo ngày
        if type_ana == '1':
            result = date_report(result_query)
            for key, value in result.items():
                key = key.strftime('%Y/%m/%d')
                list_view.update({key: "{:,}".format(value)})

        # thống kê theo tháng
        if type_ana == '2':
            result = month_report(result_query)
            for key, value in result.items():
                key = key.strftime('%Y/%m')
                key = key[:7]
                list_view.update({key: "{:,}".format(value)})

        # thống kê theo năm
        elif type_ana == '3':
            result = year_report(result_query)
            for key, value in result.items():
                key = key.strftime('%Y')
                key = key[:4]
                list_view.update({key: "{:,}".format(value)})

        #thống kê theo quý
        elif type_ana == '4':
            result = quy_report(result_query)
            for key, value in result.items():
               list_view.update({key: "{:,}".format(value)})


        print("list view: ",list_view)

        context = {
            'date_begin': date_begin,
            'date_end': date_end,
            'type': type_view,
            'list': result_query,
            'result': list_view,
            'form': form}

        return render(request, "homepage/base/tables_analytics.html", context)
    else:
        return HttpResponse("Method is not POST")


def date_report(list):
    result = {}
    for item in list:
        item.update(status = 'True')

    for item in list:
        if item['status']:
            tmp = 0
            for item2 in list:
                if item2['ngayLap'] == item['ngayLap']:
                    tmp += item2['tongTien']
                    item2['status'] = False
                node = {item['ngayLap']: tmp}
            result.update(node)
    return result


def month_report(list):
    result = {}
    for item in list:
        item['status'] = True

    for item in list:
        if item['status']:
            tmp = 0
            for item2 in list:
                if item2['ngayLap'].year == item['ngayLap'].year and item2['ngayLap'].month == item['ngayLap'].month:
                    tmp += item2['tongTien']
                    item2['status'] = False
                node = {item['ngayLap']: tmp}
            result.update(node)
    return result


def year_report(list):
    result = {}
    for item in list:
        item['status'] = True

    for item in list:
        if item['status']:
            tmp = 0
            for item2 in list:
                if item2['ngayLap'].year == item['ngayLap'].year:
                    tmp += item2['tongTien']
                    item2['status'] = False
                node = {item['ngayLap']: tmp}
            result.update(node)
    return result


def quy_report(list):
    tmp = month_report(list)
    dict = []
    for key, value in tmp.items():
        dict.append({'ngayLap': key, 'tongTien' : value, 'status': True})

    result = {}
    for item in dict:
        if item['status']:
            year = item['ngayLap'].year
            sum_tmp = 0

            # tinh doanh thu quý 1
            for item2 in dict:
                if year == item2['ngayLap'].year and item2['ngayLap'].month in [1, 2, 3] and item2['status'] == True:
                    sum_tmp += item2['tongTien']
                    item2['status'] = False
                    result.update({'quý 1 năm '+ str(year): sum_tmp})

            # tính doanh thu quý 2
            for item2 in dict:
                if year == item2['ngayLap'].year and item2['ngayLap'].month in [4, 5, 6] and item2['status'] == True:
                    sum_tmp += item2['tongTien']
                    item2['status'] = False
                    result.update({'quý 2 năm ' + str(year): sum_tmp})

            # tính doanh thu quý 3
            for item2 in dict:
                if year == item2['ngayLap'].year and item2['ngayLap'].month in [7, 8, 9] and item2['status'] == True:
                    sum_tmp += item2['tongTien']
                    item2['status'] = False
                    result.update({'quý 3 năm ' + str(year): sum_tmp})

            # tính doanh thu quý 4
            for item2 in dict:
                if year == item2['ngayLap'].year and item2['ngayLap'].month in [10, 11, 12] and item2['status'] == True:
                    sum_tmp += item2['tongTien']
                    item2['status'] = False
                    result.update({'quý 4 năm ' + str(year): sum_tmp})

    return result


def chart(request):
    return render(request, "homepage/base/charts.html")
