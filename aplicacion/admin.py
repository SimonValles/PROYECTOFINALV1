from django.contrib import admin
from .models import Articulo, Vendedor, Proveedor, Ventas, Avatar

# Register your models here.
admin.site.register(Articulo)
admin.site.register(Vendedor)
admin.site.register(Proveedor)
admin.site.register(Ventas)
admin.site.register(Avatar)