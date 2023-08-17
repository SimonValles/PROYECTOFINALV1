from django.urls import path
from .views import *

from django.contrib.auth.views import LogoutView

urlpatterns = [
    path('', index, name="inicio"),
    #path('articulos/', articulos, name="articulos"), estas rutas fueron sustituidas por CBV
    #path('vendedores/', vendedores, name="vendedores"),
    #path('proveedores/', proveedores, name="proveedores"),
    #path('ventas/', ventas, name="ventas"),
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
    #=============CRUD===============
    #View
    path('articulos/', ArticuloList.as_view(), name="articulos"),
    path('vendedores/', VendedorList.as_view(), name="vendedores"),
    path('proveedores/', ProveedorList.as_view(), name="proveedores"),
    path('ventas/', VentasList.as_view(), name="ventas"),
    #Create
    path('create_articulo/', ArticuloCreate.as_view(), name="create_articulo"),
    path('create_vendedor/', VendedorCreate.as_view(), name="create_vendedor"),
    path('create_proveedor/', ProveedorCreate.as_view(), name="create_proveedor"),
    path('create_venta/', VentaCreate.as_view(), name="create_venta"),
    #Detail
    path('detail_articulo/<int:pk>/', ArticuloDetail.as_view(), name="detail_articulo"),
    path('detail_vendedor/<int:pk>/', VendedorDetail.as_view(), name="detail_vendedor"),
    path('detail_proveedor/<int:pk>/', ProveedorDetail.as_view(), name="detail_proveedor"),
    path('detail_venta/<int:pk>/', VentaDetail.as_view(), name="detail_venta"),
    #Update
    path('update_articulo/<int:pk>/', ArticuloUpdate.as_view(), name="update_articulo"),
    path('update_vendedor/<int:pk>/', VendedorUpdate.as_view(), name="update_vendedor"),
    path('update_proveedor/<int:pk>/', ProveedorUpdate.as_view(), name="update_proveedor"),
    path('update_venta/<int:pk>/', VentaUpdate.as_view(), name="update_venta"),
    #Delete
    path('delete_articulo/<int:pk>/', ArticuloDelete.as_view(), name="delete_articulo"),
    path('delete_vendedor/<int:pk>/', VendedorDelete.as_view(), name="delete_vendedor"),
    path('delete_proveedor/<int:pk>/', ProveedorDelete.as_view(), name="delete_proveedor"),
    path('delete_venta/<int:pk>/', VentaDelete.as_view(), name="delete_venta"),
    #===================logIn logOut Registro===========================
    path('login/', login_request, name="login"),
    path('logout/', LogoutView.as_view(template_name='aplicacion/logout.html'), name="logout"),
    path('register/', register, name="register"),
    path('editar_perfil/', editarPerfil, name="editar_perfil"),
    path('agregar_avatar/', agregarAvatar, name="agregar_avatar"),
]