from django import forms
from .models import CTDanhGia


class danhGiaForm(forms.ModelForm):
    class Meta:
        model = CTDanhGia
        fields = ('maKH','maMon','rating', 'nhanXet', 'hinhAnh')

