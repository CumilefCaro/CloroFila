from django.urls import path
from .views import *

urlpatterns = [
    path('', index, name="index"),
    path('indexLogeado', indexLogeado, name="indexLogeado"),
    path('carrito', carrito, name="carrito"),
    path('registro/', registro, name="registro"),
    path('contacto/', contacto, name="contacto"),
    path('login/', login, name="login"),
    path('galeria/', galeria, name="galeria"),
    path('home/', home, name="home"),
    path('addproducto/', addproducto, name="addproducto"),
    path('listarProductos/', listarProductos, name="listarProductos"),
    path('modificarProducto/<id>/', modificarProducto, name="modificarProducto"),
    path('eliminarProducto/<id>/', eliminarProducto, name="eliminarProducto")



    

]
