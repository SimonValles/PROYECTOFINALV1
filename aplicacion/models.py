from django.db import models
from django.contrib.auth.models import User

# Create your models here.
#===================Articulo=========================
class Articulo(models.Model):
    codigo = models.CharField(max_length=50)
    nombre = models.CharField(max_length=50)
    marca = models.CharField(max_length=50)
    
    def __str__(self):
        return f"{self.nombre}, {self.marca} (Cod. {self.codigo})"



#===================Vendedor=========================   
class Vendedor(models.Model):
    nombre = models.CharField(max_length=50)
    apellido = models.CharField(max_length=50)
    dni = models.CharField(max_length=15)#ingresar con puntos divisorios
    telefono = models.CharField(max_length=20)
    
    def __str__(self):
        return f"{self.nombre} {self.apellido} (dni:{self.dni})"



#===================Proveedor=========================    
class Proveedor(models.Model):
    razonSocial = models.CharField(max_length=50)
    domicilio = models.CharField(max_length=50)
    cuit = models.CharField(max_length=50)# Se debe ingresar en la siguiente forma XX-XXXXXXXX-X
    email = models.EmailField()
    
    def __str__(self):
        return f"{self.razonSocial} (CUIT: {self.cuit})"



#===================Ventas=========================    
class Ventas(models.Model):
    fecha = models.DateField()
    codigo = models.CharField(max_length=50)
    producto = models.CharField(max_length=50)
    cantidad = models.IntegerField()
    
    def __str__(self):
        return f"{self.producto} (cod. {self.codigo})"
    
    
#===================ABOUT=========================    
class About(models.Model):
    resumen = models.CharField(max_length=1000)
    
    def __str__(self):
        return f"{self.resumen}"
    
#===================AVATAR=========================    
class Avatar(models.Model):
    imagen = models.ImageField(upload_to="avatares")
    user = models.ForeignKey(User, on_delete= models.CASCADE)
    
    def __str__(self):
        return f"{self.user} [{self.imagen}]"
