from django import  forms
from django.forms import ModelForm
from .models import Producto


class ProductoForm(forms.ModelForm):
    class Meta:
        model = Producto
        fields = ['id_producto', 'nombre_producto', 'stock', 'precio', 'fecha_recepcion']

        widgets = {
            'id_producto': forms.TextInput(attrs={'class': 'form-control'}),
            'nombre_producto': forms.TextInput(attrs={'class': 'form-control'}),
            'stock': forms.NumberInput(attrs={'class': 'form-control'}),
            'precio': forms.NumberInput(attrs={'class': 'form-control'}),
            'fecha_recepcion': forms.DateInput(attrs={'class': 'form-control'}),
        }