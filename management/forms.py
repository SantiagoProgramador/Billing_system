from django import forms
from .models import Bill, BillDetail, Product

class BillDetailForm(forms.Form):
    product = forms.ModelChoiceField(queryset=Product.objects.all(), widget=forms.Select(attrs={'class': 'form-control'}))
    quantity = forms.IntegerField(min_value=1, widget=forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Quantity'}))

class BillForm(forms.Form):
    details = forms.CharField(widget=forms.HiddenInput()) 
