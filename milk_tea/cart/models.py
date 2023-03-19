from django.db import models

from product.models import Mon, CTGia
from customer.models import KhachHang
# Create your models here.


class GioHang(models.Model):

    maGH = models.AutoField(primary_key=True)
    maKH= models.ForeignKey(KhachHang, on_delete=models.CASCADE)
    trangThai = models.BooleanField(default=True)
    
    def __str__(self):
        return str(self.maGH)
    

class CTGioHang(models.Model):

    maCTGH = models.AutoField(primary_key=True)
    maGH = models.ForeignKey(GioHang, on_delete=models.CASCADE)
    maMon= models.ForeignKey(Mon, on_delete=models.CASCADE)
    giaMon= models.DecimalField(default=0, max_digits=9, decimal_places=3)
    size= models.CharField(max_length= 2, blank=True)
    soLuong= models.IntegerField(default=1)

    
    def __str__(self):
        return str(self.maCTGH)
    



