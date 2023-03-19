from django.contrib import admin

from .models import KhachHang
# Register your models here.

class KhachHangAdmin(admin.ModelAdmin):
    list_display= ('maKH', 'hoKH','tenKH', 'sdt', 'email', 'diaChi')


admin.site.register(KhachHang,KhachHangAdmin)
