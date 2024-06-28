from django import  forms
from django.forms import ModelForm
from .models import Producto, Marca


class ProductoForm(forms.ModelForm):
    class Meta:
        model = Producto
        fields = ['id_producto', 'nombre_producto', 'descripcion','marca','stock', 'precio', 'fecha_recepcion', 'tallas_disponibles']

        widgets = {
            'id_producto': forms.TextInput(attrs={'class': 'form-control'}),
            'nombre_producto': forms.TextInput(attrs={'class': 'form-control'}),
            'descripcion': forms.TextInput(attrs={'class': 'form-control'}),
            'marca': forms.TextInput(attrs={'class': 'form-control'}),
            'stock': forms.NumberInput(attrs={'class': 'form-control'}),
            'precio': forms.NumberInput(attrs={'class': 'form-control'}),
            'fecha_recepcion': forms.DateInput(attrs={'class': 'form-control'}),
            'tallas_disponibles': forms.TextInput(attrs={'class': 'form-control'}),
        }


