from django.contrib import admin

from .models import GioHang, CTGioHang
# Register your models here.


class GHAdmin(admin.ModelAdmin):
    list_display= ('maGH', 'maKH','trangThai')

class CTGHAdmin(admin.ModelAdmin):
    list_display= ('maCTGH', 'maGH','maMon', 'giaMon','size','soLuong')


admin.site.register(GioHang,GHAdmin)
admin.site.register(CTGioHang,CTGHAdmin)
