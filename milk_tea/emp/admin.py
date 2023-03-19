from django.contrib import admin
from .models import Nhanvien
# Register your models here.

class NVAdmin(admin.ModelAdmin):
    list_display= ('maNV', 'hoNV','tenNV', 'sdt', 'email', 'diaChi')


admin.site.register(Nhanvien,NVAdmin)