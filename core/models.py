from django.db import models
from django.contrib.auth.models import User, AbstractUser
from datetime import datetime


# Create your models here.



class Categoria(models.Model):
    nombre = models.CharField(max_length=50)

    def __str__(self):
        return self.nombre

class Producto(models.Model):
    nombre = models.CharField(max_length=50) 
    precio = models.IntegerField()
    descripcion = models.TextField()
    exterior = models.BooleanField()
    categoria = models.ForeignKey(Categoria, on_delete=models.PROTECT) 
    imagen = models.ImageField(null=True, blank=True)
    stock = models.IntegerField(default=0)
    creado_en = models.DateField(auto_now_add=True)
    modificado_en = models.DateField(auto_now=True)

    def __str__(self):
       return self.nombre






     