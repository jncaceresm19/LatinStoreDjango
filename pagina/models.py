from django.db import models

class Producto(models.Model):
    id_producto = models.CharField(max_length=5, primary_key=True)
    nombre_producto = models.CharField(max_length=100)
    stock = models.IntegerField(default=0)
    precio = models.IntegerField(default=0)
    fecha_recepcion = models.DateField()

    def __str__(self):
        return self.nombre_producto