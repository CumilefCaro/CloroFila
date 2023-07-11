from django.urls import path
from .views import *

urlpatterns = [
    path('', index, name="index"),
    path('registro/', registro, name="registro"),
    path('contacto/', contacto, name="contacto"),
    path('galeria/', galeria, name="galeria"),
    path('home/', home, name="home"),
    path('addproducto/', addproducto, name="addproducto"),
    path('listarProductos/', listarProductos, name="listarProductos"),
    path('modificarProducto/<id>/', modificarProducto, name="modificarProducto"),
    path('eliminarProducto/<id>/', eliminarProducto, name="eliminarProducto"),
  

]
