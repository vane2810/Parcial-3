from django.db import models
from django.contrib.auth.models import Group

Group.objects.get_or_create(name='Gerente')
Group.objects.get_or_create(name='Cliente')

#Entidad proveedores
class Proveedores(models.Model):
    nombre = models.CharField(max_length=100)
    marca = models.CharField(max_length=100)
    contacto = models.CharField(max_length=20)

    def __str__(self):
        return self.nombre


#Entidad articulos
class Articulos(models.Model):
    nombre = models.CharField(max_length=100)
    precio = models.FloatField()
    descripcion = models.CharField(max_length=255)
    proveedorID = models.ForeignKey(Proveedores, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.nombre


#Entidad clientes
class Clientes(models.Model):
    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100)
    contacto = models.CharField(max_length=20)
    articuloID = models.ForeignKey(Articulos, on_delete=models.CASCADE) 

    def __str__(self):
        return self.nombre