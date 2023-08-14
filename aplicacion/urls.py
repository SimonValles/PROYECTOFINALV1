from django.urls import path
from .views import *

urlpatterns = [
    path('', index, name="inicio"),
    path('articulos/', articulos, name="articulos"),
    path('vendedores/', vendedores, name="vendedores"),
    path('proveedores/', proveedores, name="proveedores"),
    path('ventas/', ventas, name="ventas"),
    # urls para forms
    path('articulos_form/', articulosForm, name="articulos_form"),
    path('vendedores_form/', vendedoresForm, name="vendedores_form"), 
    path('proveedores_form/', proveedoresForm, name="proveedores_form"), 
    path('ventas_form/', ventasForm, name="ventas_form"),   
    # urls para funcion buscar
    path('buscar_codigo/', buscarCodigo, name="buscar_codigo"),
    path('buscar2/', buscar2, name="buscar2"), 
    path('buscar_proveedor/', buscarProveedor, name="buscar_proveedor"),
    path('buscar3/', buscar3, name="buscar3"),
    path('buscar_vendedor/', buscarVendedor, name="buscar_vendedor"),
    path('buscar4/', buscar4, name="buscar4"),
    path('buscar_venta/', buscarVenta, name="buscar_venta"),
    path('buscar5/', buscar5, name="buscar5"), 
    # about me
    path('about/', about, name="about"),
    #updates
    path('update_articulo/<id_articulo>/', updateArticulo, name="update_articulo"),
    path('update_vendedor/<id_vendedor>/', updateVendedor, name="update_vendedor"),
    path('update_proveedor/<id_proveedor>/', updateProveedor, name="update_proveedor"),
    path('update_venta/<id_venta>/', updateVenta, name="update_venta"),
    #deletes
    path('delete_articulo/<id_articulo>/', deleteArticulo, name="delete_articulo"),
    path('delete_vendedor/<id_vendedor>/', deleteVendedor, name="delete_vendedor"),
    path('delete_proveedor/<id_proveedor>/', deleteProveedor, name="delete_proveedor"),
    path('delete_venta/<id_venta>/', deleteVenta, name="delete_venta"),
    #creates
    path('create_articulo/', createArticulo, name="create_articulo"),
    path('create_vendedor/', createVendedor, name="create_vendedor"),
    path('create_proveedor/', createProveedor, name="create_proveedor"),
    path('create_venta/', createVenta, name="create_venta"),
    #CBV
    path('articulos/', ArticuloList.as_view(), name="articulos"),
]