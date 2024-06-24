from django.contrib import admin
from .models import Producto, Marca, Cliente, Pedido

# Register your models here.
admin.site.register(Producto)
admin.site.register(Marca)
admin.site.register(Cliente)
admin.site.register(Pedido)
