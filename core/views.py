from django.shortcuts import render,redirect, get_object_or_404
from.forms import ProductoForm, Producto, CustomUserCreationForm
from django.contrib import messages
from django.contrib.auth import authenticate, login
from .models import *
from django.core.paginator import Paginator
from django.http import Http404

# Create your views here.

def index(request):
     return render(request, 'core/index.html')



def contacto(request):
     return render(request, 'core/contacto.html')

     return render(request, 'core/home.html')


def galeria(request):
     productos = Producto.objects.all()
     data ={
          'productos':productos
     }
     return render(request, 'core/galeria.html',data)
     

def home(request):
     return render(request, 'core/home.html')
def addproducto(request):
     data = {
          'form' : ProductoForm()

     }
     
     if request.method == 'POST':
          formulario = ProductoForm(request.POST,files=request.FILES)
          if formulario.is_valid():
               formulario.save()
              
          else:     
               data ['form'] = formulario
     return render(request, 'core/producto/addproducto.html', data)


def listarProductos(request):
     prod =Producto.objects.all()
     data = {
          'prod' : prod
     }
       
     
     return render(request,'core/producto/listarProductos.html', data)


def modificarProducto(request, id):
     produ = get_object_or_404(Producto, id=id)
     data ={
          'form' : ProductoForm(instance=produ)
     }
     if request.method == 'POST':
          formulario = ProductoForm(data=request.POST,instance=produ, files=request.FILES)
          if formulario.is_valid():
               formulario.save()
               messages.success(request, "Modificado correctamente")
               return redirect(to="listarProductos")
          data ['form'] = formulario

     return render(request,'core/producto/modificarProducto.html', data)

def eliminarProducto(request, id):
     produ = get_object_or_404(Producto, id=id)
     produ.delete()
     
     
     return redirect(to="listarProductos")

def registro(request):
     data ={
         'form': CustomUserCreationForm
     }
     if request.method == 'POST':
         formulario = CustomUserCreationForm(data=request.POST)
         if formulario.is_valid():
              formulario.save()
              user = authenticate(username=formulario.cleaned_data ["username"], password=formulario.cleaned_data["password1"])
              login(request, user )
              messages.success(request, "Registrado correctamente")
              return redirect(to=home)
              
    
     return render(request, 'registration/registro.html',data)





