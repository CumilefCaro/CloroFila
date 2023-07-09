
from django.contrib import admin
from.models import Categoria, Producto

class ProductoAdmin(admin.ModelAdmin):
    list_display = ['nombre','precio','descripcion','exterior','categoria','stock']
    list_editable= ['precio','exterior','categoria','stock']
    
    


# Register your models here.
admin.site.register(Categoria)
admin.site.register(Producto, ProductoAdmin)






