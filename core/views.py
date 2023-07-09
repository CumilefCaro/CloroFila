from django.shortcuts import render,redirect, get_object_or_404
from.forms import *
from django.contrib import messages



# Create your views here.
def carrito(request):
     return render(request, 'core/carrito.html')
def indexLogeado(request):
     return render(request, 'core/indexLogeado.html')
def index(request):
     return render(request, 'core/index.html')

def registro(request):
     return render(request, 'core/registro.html')

def contacto(request):
     return render(request, 'core/contacto.html')

     return render(request, 'core/home.html')



def galeria(request):
     productos = Producto.objects.all()
     data ={
          'productos':productos
     }
     return render(request, 'core/galeria.html',data)
     
def login(request):
     return render(request, 'core/login.html')
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
               data ['mensaje'] = "Guardado correctamente"
          else:     
               data ['form'] = formulario
     return render(request, 'core/producto/addproducto.html', data)


def listarProductos(request):
     prod =Producto.objects.all()

     data = {
          'prod':prod
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
