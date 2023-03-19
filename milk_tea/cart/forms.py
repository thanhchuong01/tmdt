from django import forms
from .models import CTGioHang

class CtGHForm(forms.ModelForm):
    class Meta:
        model = CTGioHang
        fields = ['giaMon', 'soLuong']