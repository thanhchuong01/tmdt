from django.db import models


from product.models import Mon
from customer.models import KhachHang

# Create your models here.

class KhuyenMai(models.Model):

    maKM = models.AutoField(primary_key=True)
    tenKM= models.CharField(max_length= 50)
    code= models.CharField(max_length= 10)
    phantramKM= models.IntegerField(default=1)
    ngayHetHan= models.DateField()
    trangThai= models.BooleanField(default=True)

    
    def __str__(self):
        return f"{self.code}, {self.phantramKM}"


class ThanhToan(models.Model):

    maTT = models.AutoField(primary_key=True)
    tenTT= models.CharField(max_length= 50)

    
    def __str__(self):
        return f"{self.tenTT}"
    


trangthai= (
        ('0', 'Hủy'),
        ('1', 'Chưa xác nhận'),
        ('2', 'Đã xác nhận'),
        ('3', 'Đang chuẩn bị'),
        ('4', 'Đang vận chuyển'),
        ('5', 'Hoàn thành')
    )

class DonHang(models.Model):

    maDH = models.AutoField(primary_key=True)
    maKH= models.ForeignKey(KhachHang, on_delete=models.CASCADE)
    tongTien= models.DecimalField(default=0, max_digits=9, decimal_places=3)
    ngayLap = models.DateTimeField(auto_now_add= True)
    trangThaiDH= models.CharField(max_length= 50, choices=trangthai, default=1)
    maKM= models.ForeignKey(KhuyenMai, on_delete=models.SET_NULL, null=True, blank=True)
    maTT= models.ForeignKey(ThanhToan, on_delete=models.SET_NULL, null=True, blank=True)
    diachi= models.CharField(max_length= 200,null=True, blank=True)
    # xaphuong= models.CharField(max_length= 50,null=True, blank=True)
    # quanhuyen= models.CharField(max_length= 50,null=True, blank=True)
    # tinhtp= models.CharField(max_length= 50,null=True, blank=True)
    sdt= models.CharField(max_length= 50,null=True, blank=True)
    hoten= models.CharField(max_length= 50,null=True, blank=True)


    
    def __str__(self):
        return f"{self.maDH}, {self.maKH}, {self.tongTien}"


class CTDonHang(models.Model):

    maCTDH = models.AutoField(primary_key=True)
    maDH= models.ForeignKey(DonHang, on_delete=models.CASCADE)
    maMon= models.ForeignKey(Mon, on_delete=models.CASCADE)
    giaMon= models.DecimalField(default=0, max_digits=9, decimal_places=3)
    soLuong= models.IntegerField(default=1)

    
    def __str__(self):
        return f"{self.maCTDH}, {self.maDH}, {self.maMon},{self.giaMon}"



