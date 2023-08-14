from django.shortcuts import redirect, render
from django.http import HttpResponse
from django.urls import reverse_lazy
from aplicacion.forms import ArticuloForm, ProveedorForm, VendedorForm, VentasForm
from .models import *
from .forms import *
from django.views.generic import ListView

# Create your views here.


def index(request):
    return render(request, "aplicacion/base.html")

#=================ARTICULOS===============================

def articulos(request):
    ctx = {"articulos": Articulo.objects.all()}
    return render(request, 'aplicacion/articulos.html', ctx)

def articulosForm(request):
    if request.method == "POST":
        miForm = ArticuloForm(request.POST)
        print(miForm)
        if miForm.is_valid():
            articulo_codigo = miForm.cleaned_data.get('codigo')
            articulo_nombre = miForm.cleaned_data.get('nombre')
            articulo_marca = miForm.cleaned_data.get('marca')
            articulo = Articulo(codigo=articulo_codigo, 
                                nombre=articulo_nombre, 
                                marca=articulo_marca)
            articulo.save()
            return render(request, 'aplicacion/base.html')
    else:
        miForm = ArticuloForm()
        
    return render(request, 'aplicacion/articulosForm.html', {"form":miForm})

def updateArticulo(request,id_articulo):
    articulo = Articulo.objects.get(id=id_articulo)
    if request.method == "POST":
        miForm = ArticuloForm(request.POST)
        if miForm.is_valid():
            articulo_codigo = miForm.cleaned_data.get('codigo')
            articulo_nombre = miForm.cleaned_data.get('nombre')
            articulo_marca = miForm.cleaned_data.get('marca')
            articulo.save()
            return redirect(reverse_lazy('articulos'))
    else:
        miForm = ArticuloForm(initial={'codigo':articulo_codigo, 
                                       'domicilio':articulo_nombre, 
                                       'cuit':articulo_marca})
    return render(request, "aplicacion/articulosForm2.html", {'form': miForm})


def deleteArticulo(request,id_articulo):
    articulo = Proveedor.objects.get(id=id_articulo)
    articulo.delete()
    return redirect(reverse_lazy('articulos'))

def createArticulo(request):
    if request.method == "POST":
        miForm = ArticuloForm(request.POST)
        print(miForm)
        if miForm.is_valid():
            articulo_codigo = miForm.cleaned_data.get('codigo')
            articulo_nombre = miForm.cleaned_data.get('nombre')
            articulo_marca = miForm.cleaned_data.get('marca')
            articulo = Articulo(codigo=articulo_codigo, 
                                  domicilio=articulo_nombre, 
                                  cuit=articulo_marca)
            articulo.save()
            return redirect(reverse_lazy('proveedores'))
    else:
        miForm = ArticuloForm()
        
    return render(request, 'aplicacion/articulosForm.html', {"form":miForm})



#=================PROVEEDORES===============================

def proveedores(request):
    ctx = {"proveedores": Proveedor.objects.all()}
    return render(request, 'aplicacion/proveedores.html', ctx)

def proveedoresForm(request):
    if request.method == "POST":
        miForm = ProveedorForm(request.POST)
        print(miForm)
        if miForm.is_valid():
            proveedor_razonSocial = miForm.cleaned_data.get('razonSocial')
            proveedor_domicilio = miForm.cleaned_data.get('domicilio')
            proveedor_cuit = miForm.cleaned_data.get('cuit')
            proveedor_email = miForm.cleaned_data.get('email')
            proveedor = Proveedor(razonSocial=proveedor_razonSocial, 
                                  domicilio=proveedor_domicilio, 
                                  cuit=proveedor_cuit, 
                                  email=proveedor_email)
            proveedor.save()
            return render(request, 'aplicacion/base.html')
    else:
        miForm = ProveedorForm()
        
    return render(request, 'aplicacion/proveedoresForm.html', {"form":miForm})

def updateProveedor(request,id_proveedor):
    proveedor = Proveedor.objects.get(id=id_proveedor)
    if request.method == "POST":
        miForm = ProveedorForm(request.POST)
        if miForm.is_valid():
            proveedor.razonSocial = miForm.cleaned_data.get('razonSocial')
            proveedor.domicilio = miForm.cleaned_data.get('domicilio')
            proveedor.cuit = miForm.cleaned_data.get('cuit')
            proveedor.email = miForm.cleaned_data.get('email')
            proveedor.save()
            return redirect(reverse_lazy('proveedores'))
    else:
        miForm = ProveedorForm(initial={'razonSocial':proveedor.razonSocial, 
                                       'domicilio':proveedor.domicilio, 
                                       'cuit':proveedor.cuit,
                                       'email':proveedor.email})
    return render(request, "aplicacion/proveedoresForm2.html", {'form': miForm})


def deleteProveedor(request,id_proveedor):
    proveedor = Proveedor.objects.get(id=id_proveedor)
    proveedor.delete()
    return redirect(reverse_lazy('proveedores'))

def createProveedor(request):
    if request.method == "POST":
        miForm = ProveedorForm(request.POST)
        print(miForm)
        if miForm.is_valid():
            proveedor_razonSocial = miForm.cleaned_data.get('razonSocial')
            proveedor_domicilio = miForm.cleaned_data.get('domicilio')
            proveedor_cuit = miForm.cleaned_data.get('cuit')
            proveedor_email = miForm.cleaned_data.get('email')
            proveedor = Proveedor(razonSocial=proveedor_razonSocial, 
                                  domicilio=proveedor_domicilio, 
                                  cuit=proveedor_cuit, 
                                  email=proveedor_email)
            proveedor.save()
            return redirect(reverse_lazy('proveedores'))
    else:
        miForm = ProveedorForm()
        
    return render(request, 'aplicacion/proveedoresForm.html', {"form":miForm})


#=================VENDEDORES===============================

def vendedores(request):
    ctx = {"vendedores": Vendedor.objects.all()}
    return render(request, 'aplicacion/vendedores.html', ctx)

def vendedoresForm(request):
    if request.method == "POST":
        miForm = VendedorForm(request.POST)
        print(miForm)
        if miForm.is_valid():
            vendedor_nombre = miForm.cleaned_data.get('nombre')
            vendedor_apellido = miForm.cleaned_data.get('apellido')
            vendedor_dni = miForm.cleaned_data.get('dni')
            vendedor_telefono = miForm.cleaned_data.get('telefono')
            vendedor = Vendedor(nombre=vendedor_nombre, 
                                apellido=vendedor_apellido, 
                                dni=vendedor_dni, 
                                telefono=vendedor_telefono)
            vendedor.save()
            return render(request, 'aplicacion/base.html')
    else:
        miForm = VendedorForm()
        
    return render(request, 'aplicacion/vendedoresForm.html', {"form":miForm})

def updateVendedor(request,id_vendedor):
    vendedor = Vendedor.objects.get(id=id_vendedor)
    if request.method == "POST":
        miForm = VendedorForm(request.POST)
        if miForm.is_valid():
            vendedor.nombre = miForm.cleaned_data.get('nombre')
            vendedor.apellido = miForm.cleaned_data.get('apellido')
            vendedor.dni = miForm.cleaned_data.get('dni')
            vendedor.telefono = miForm.cleaned_data.get('telefono')
            vendedor.save()
            return redirect(reverse_lazy('vendedores'))
    else:
        miForm = VendedorForm(initial={'nombre':vendedor.nombre, 
                                       'apellido':vendedor.apellido, 
                                       'dni':vendedor.dni,
                                       'telefono':vendedor.telefono})
    return render(request, "aplicacion/vendedoresForm2.html", {'form': miForm})


def deleteVendedor(request,id_vendedor):
    vendedor = Vendedor.objects.get(id=id_vendedor)
    vendedor.delete()
    return redirect(reverse_lazy('vendedores'))

def createVendedor(request):
    if request.method == "POST":
        miForm = VendedorForm(request.POST)
        print(miForm)
        if miForm.is_valid():
            vendedor_nombre = miForm.cleaned_data.get('nombre')
            vendedor_apellido = miForm.cleaned_data.get('apellido')
            vendedor_dni = miForm.cleaned_data.get('dni')
            vendedor_telefono = miForm.cleaned_data.get('telefono')
            vendedor = Vendedor(nombre=vendedor_nombre,
                                apellido=vendedor_apellido,
                                dni=vendedor_dni,
                                telefono=vendedor_telefono)
            vendedor.save()
            return redirect(reverse_lazy('vendedores'))
    else:
        miForm = VendedorForm()
        
    return render(request, 'aplicacion/vendedoresForm.html', {"form":miForm})


#=================VENTAS===============================

def ventas(request):
    ctx = {"ventas": Ventas.objects.all()}
    return render(request, 'aplicacion/ventas.html', ctx)

def ventasForm(request):
    if request.method == "POST":
        miForm = VentasForm(request.POST)
        print(miForm)
        if miForm.is_valid():
            venta_fecha = miForm.cleaned_data.get('fecha')
            venta_codigo = miForm.cleaned_data.get('codigo')
            venta_producto = miForm.cleaned_data.get('producto')
            venta_cantidad = miForm.cleaned_data.get('cantidad')            
            venta = Ventas(fecha=venta_fecha, 
                           codigo=venta_codigo, 
                           producto=venta_producto, 
                           cantidad=venta_cantidad)
            venta.save()
            return render(request, 'aplicacion/base.html')
    else:
        miForm = VentasForm()
        
    return render(request, 'aplicacion/ventasForm.html', {"form":miForm})

def updateVenta(request,id_venta):
    venta = Ventas.objects.get(id=id_venta)
    if request.method == "POST":
        miForm = VentasForm(request.POST)
        if miForm.is_valid():
            venta.fecha = miForm.cleaned_data.get('fecha')
            venta.codigo = miForm.cleaned_data.get('codigo')
            venta.producto = miForm.cleaned_data.get('producto')
            venta.cantidad = miForm.cleaned_data.get('cantidad')
            venta.save()
            return redirect(reverse_lazy('ventas'))
    else:
        miForm = VentasForm(initial={'fecha':venta.fecha, 
                                     'codigo':venta.codigo, 
                                     'producto':venta.producto,
                                     'cantidad':venta.cantidad})
    return render(request, "aplicacion/ventasForm2.html", {'form': miForm})

def deleteVenta(request,id_venta):
    venta = Ventas.objects.get(id=id_venta)
    venta.delete()
    return redirect(reverse_lazy('ventas'))


def createVenta(request):
    if request.method == "POST":
        miForm = VentasForm(request.POST)
        print(miForm)
        if miForm.is_valid():
            venta_fecha = miForm.cleaned_data.get('fecha')
            venta_codigo = miForm.cleaned_data.get('codigo')
            venta_producto = miForm.cleaned_data.get('producto')
            venta_cantidad = miForm.cleaned_data.get('cantidad')
            venta = Ventas(fecha=venta_fecha,
                           codigo=venta_codigo,
                           producto=venta_producto,
                           cantidad=venta_cantidad)
            venta.save()
            return redirect(reverse_lazy('ventas'))
    else:
        miForm = VentasForm()
        
    return render(request, 'aplicacion/ventasForm.html', {"form":miForm})


#=================ABOUT ME===============================

def about(request):
    ctx = {"about": About.objects.all()}
    return render(request, 'aplicacion/about.html', ctx)



#=================BUSCAR CODIGO===============================

def buscarCodigo(request):
    return render(request, "aplicacion/buscarCodigo.html")

def buscar2(request):
    if request.GET['codigo']:
        codigo = request.GET['codigo']
        articulos = Articulo.objects.filter(codigo__icontains=codigo)
        return render(request, 
                      "aplicacion/resultadosCodigo.html",
                      {"codigo": codigo, "articulos": articulos})
    return HttpResponse("No se ingresaron datos para realizar busqueda")

#=================BUSCAR PROVEEDOR===============================

def buscarProveedor(request):
    return render(request, "aplicacion/buscarProveedor.html")

def buscar3(request):
    if request.GET['cuit']:
        cuit = request.GET['cuit']
        proveedores = Proveedor.objects.filter(cuit__icontains=cuit)
        return render(request, 
                      "aplicacion/resultadosProveedor.html",
                      {"ciut": cuit, "proveedores": proveedores})
    return HttpResponse("No se ingresaron datos para realizar busqueda")

#=================BUSCAR VENDEDOR===============================

def buscarVendedor(request):
    return render(request, "aplicacion/buscarVendedor.html")

def buscar4(request):
    if request.GET['dni']:
        dni = request.GET['dni']
        vendedores = Vendedor.objects.filter(dni__icontains=dni)
        return render(request, 
                      "aplicacion/resultadosVendedores.html",
                      {"dni": dni, "vendedores": vendedores})
    return HttpResponse("No se ingresaron datos para realizar busqueda")

#=================BUSCAR VENTA===============================

def buscarVenta(request):
    return render(request, "aplicacion/buscarVenta.html")

def buscar5(request):
    if request.GET['codigo']:
        codigo = request.GET['codigo']
        ventas = Ventas.objects.filter(codigo__icontains=codigo)
        return render(request, 
                      "aplicacion/resultadosVentas.html",
                      {"codigo": codigo, "ventas": ventas})
    return HttpResponse("No se ingresaron datos para realizar busqueda")


#=========================class based view======================

class ArticuloList(ListView):
    model = Articulo
    