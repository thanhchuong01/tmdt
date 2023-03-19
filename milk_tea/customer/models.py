from django.db import models

# Create your models here.

class KhachHang(models.Model):

    maKH = models.AutoField(primary_key=True)
    # maDM= models.ForeignKey(Danhmuc, on_delete=models.CASCADE)
    hoKH = models.CharField(max_length= 10)
    tenKH = models.CharField(max_length= 10)
    sdt= models.IntegerField(default= 0)
    email = models.EmailField(default= None, unique=True)
    diaChi= models.CharField(max_length= 50)

    def __str__(self):
        return f"{self.hoKH} {self.tenKH}"

