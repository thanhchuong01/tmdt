from django.urls import path
from . import views


urlpatterns = [
    path('nhanvien/index/', views.index, name='aa'),
    path('nhanvien/xuly/', views.view, name='xuly'),
    path('nhanvien/delete/<input_id>', views.delete_dh, name='del_dh'),
    path('nhanvien/accept/<input_id>', views.accept_dh, name='accept_dh'),
    path('nhanvien/process/<input_id>', views.process_dh, name='process_dh'),
    path('nhanvien/transport/<input_id>', views.transport_dh, name='transport_dh'),
    path('nhanvien/done/<input_id>', views.done_dh, name='done_dh'),


    path('nhanvien/view/', views.statistic, name='statistic'),
    path('nhanvien/views/', views.view_time, name='views_time'),
    path('nhanvien/chart/', views.chart, name='chart'),
]
