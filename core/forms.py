from django import forms
from django.forms import ModelForm
from .models import *

class ProductoForm(ModelForm):

    class Meta:
        model = Producto
        fields = '__all__'

class CategoriaForm(ModelForm):

    class Meta:
        model = Categoria
        fields = '__all__'