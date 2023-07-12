from django.urls import path, include 
from .views import *
from  rest_framework import routers 
router = routers.DefaultRouter()
router.register('producto', ProductoViewsets)



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
    path('api/', include(router.urls)),
  

]
