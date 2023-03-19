from django.contrib import admin

from .models import CTDonHang, DonHang, KhuyenMai, ThanhToan
# Register your models here.


class DHAdmin(admin.ModelAdmin):
    list_display= ('maDH', 'maKH','tongTien','ngayLap','trangThaiDH','maKM','maTT','diachi','sdt','hoten')

class CTDHAdmin(admin.ModelAdmin):
    list_display= ('maCTDH', 'maDH','maMon', 'giaMon','soLuong')

class KMAdmin(admin.ModelAdmin):
    list_display= ('maKM', 'tenKM','code', 'phantramKM','ngayHetHan','trangThai')

class TTAdmin(admin.ModelAdmin):
    list_display= ('maTT', 'tenTT')


admin.site.register(DonHang,DHAdmin)
admin.site.register(CTDonHang,CTDHAdmin)
admin.site.register(KhuyenMai,KMAdmin)
admin.site.register(ThanhToan,TTAdmin)
