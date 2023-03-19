from django.db import models
from django.core.files.storage import FileSystemStorage
from django.db.models import Count

from customer.models import KhachHang

# Create your models here.

# fs = FileSystemStorage(location='/static/homepage/')
    

class Danhmuc(models.Model):

    maDM = models.AutoField(primary_key=True)
    tenDM = models.CharField(max_length= 15)
    hinhAnhDM = models.ImageField(upload_to='dm', null=True, default= None)
    ngayCN = models.DateTimeField(auto_now_add= True)
    
    def __str__(self):
        return str(self.tenDM)
    

sizes= (
        ('M', 'M'),
        ('L', 'L')
    )

class CTGia(models.Model):
    maGia = models.AutoField(primary_key=True)
    size = models.CharField(max_length= 2, default='L') 
    giaSize= models.DecimalField(default=0, max_digits=9, decimal_places=3)
    
 
    def __str__(self):
        return self.size
    


class Mon(models.Model):

    maMon = models.AutoField(primary_key=True)
    maDM= models.ForeignKey(Danhmuc, on_delete=models.CASCADE)
    # tenMon = models.CharField(max_length= 50)
    tenMon = models.TextField(max_length= 50)

    hinhAnh = models.ImageField(upload_to='img', null=False, default= None)
    moTa= models.CharField(max_length= 500)
    ngayCN = models.DateTimeField(auto_now_add= True)
    gia= models.DecimalField(default=0, max_digits=9, decimal_places=3)
    sizeMon = models.ManyToManyField(CTGia, blank=True)
    trangThaiMon= models.BooleanField(default=True)

    def __str__(self):
        return self.tenMon
    
    def get_product_price_by_size(self, id,s):
        return Mon.objects.get(pk = id).gia + CTGia.objects.get(size= s).giaSize

    def get_sizes(self):
        return "\n".join([s.size for s in self.sizeMon.all()])
    

class CTDanhGia(models.Model):
    idDanhGia = models.AutoField(primary_key=True)
    rating = models.FloatField(default=0)
    ngayDanhGia = models.DateTimeField(auto_now_add= True)
    nhanXet = models.TextField(max_length=1000)
    maKH = models.ForeignKey(KhachHang, on_delete=models.CASCADE)
    maMon = models.ForeignKey(Mon, on_delete=models.CASCADE)
    hinhAnh = models.ImageField(upload_to='img', blank=True, default=None)

    def __str__(self):
        return f"{self.idDanhGia}"


