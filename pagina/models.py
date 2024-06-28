<<<<<<< HEAD
from django.db import models

class Marca(models.Model):
    nombre = models.CharField(max_length=100)
    
    def __str__(self):
        return self.nombre

class Producto(models.Model):
    id_producto = models.CharField(max_length=5, primary_key=True)
    nombre_producto = models.CharField(max_length=100)
    descripcion = models.TextField(blank=True, null=True)  
    stock = models.IntegerField(default=0)
    precio = models.DecimalField(max_digits=10, decimal_places=2)  
    fecha_recepcion = models.DateField()
    marca = models.ForeignKey(Marca, on_delete=models.CASCADE)
    tallas_disponibles = models.CharField(max_length=100, blank=True, null=True)  

    def __str__(self):
        return self.nombre_producto

class Cliente(models.Model):
    nombre = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    direccion = models.TextField()
    
    def __str__(self):
        return self.nombre

class Pedido(models.Model):
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)
    producto = models.ForeignKey(Producto, on_delete=models.CASCADE)
    cantidad = models.IntegerField()
    fecha_pedido = models.DateField(auto_now_add=True)
    
    def __str__(self):
=======
from django.db import models

class Marca(models.Model):
    nombre = models.CharField(max_length=100)
    
    def __str__(self):
        return self.nombre

class Producto(models.Model):
    id_producto = models.CharField(max_length=5, primary_key=True)
    nombre_producto = models.CharField(max_length=100)
    descripcion = models.TextField(blank=True, null=True)  
    stock = models.IntegerField(default=0)
    precio = models.DecimalField(max_digits=10, decimal_places=2)  
    fecha_recepcion = models.DateField()
    marca = models.ForeignKey(Marca, on_delete=models.CASCADE)
    tallas_disponibles = models.CharField(max_length=100, blank=True, null=True)  

    def __str__(self):
        return self.nombre_producto

class Cliente(models.Model):
    nombre = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    direccion = models.TextField()
    
    def __str__(self):
        return self.nombre

class Pedido(models.Model):
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)
    producto = models.ForeignKey(Producto, on_delete=models.CASCADE)
    cantidad = models.IntegerField()
    fecha_pedido = models.DateField(auto_now_add=True)
    
    def __str__(self):
>>>>>>> da4c064962d8a85d73cf128fd4e29a2e01c65867
        return f"Pedido {self.id} de {self.cliente.nombre}"