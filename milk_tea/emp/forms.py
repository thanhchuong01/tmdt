from django import forms
from bootstrap_datepicker_plus.widgets import DatePickerInput


class DateForm(forms.Form):
    date_begin = forms.DateField(
        input_formats=['%d/%m/%y'],
        widget=forms.DateInput(attrs={
            'class': 'form-control datetimepicker-input',
            'data-target': '#datepicker',
            'placeholder': 'select a day',
            'type': 'date'
        })
    )
    date_end = forms.DateField(
        input_formats=['%d/%m/%Y'],
        widget=forms.DateInput(attrs={
            'class': 'form-control datetimepicker-input',
            'data-target': '#datepicker',
            'placeholder' : 'select a day',
            'type' : 'date'
        })
    )
    LIST_CHOICE = [('1','Ngày'), ('2', 'Tháng'), ('3', 'Năm'), ('4', 'Quý')]
    type_ana = forms.CharField(
        widget=forms.Select(choices=LIST_CHOICE, attrs={'class': 'type_analytics_droplist form-control'}))
