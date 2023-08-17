from django.shortcuts import redirect, render
from django.http import HttpResponse
from django.urls import reverse_lazy
from aplicacion.forms import ArticuloForm, ProveedorForm, VendedorForm, VentasForm
from .models import *
from .forms import *

from django.views.generic import ListView
from django.views.generic import CreateView
from django.views.generic import UpdateView
from django.views.generic import DetailView
from django.views.generic import DeleteView

from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required

# Create your views here.


def index(request):
    return render(request, "aplicacion/base.html")

#=================ARTICULOS forms===============================

@login_required
def articulos(request):
    ctx = {"articulos": Articulo.objects.all()}
    return render(request, 'aplicacion/articulos.html', ctx)

@login_required
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


#=================PROVEEDORES forms===============================

@login_required
def proveedores(request):
    ctx = {"proveedores": Proveedor.objects.all()}
    return render(request, 'aplicacion/proveedores.html', ctx)

@login_required
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


#=================VENDEDORES forms===============================

@login_required
def vendedores(request):
    ctx = {"vendedores": Vendedor.objects.all()}
    return render(request, 'aplicacion/vendedores.html', ctx)

@login_required
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


#=================VENTAS forms===============================

@login_required
def ventas(request):
    ctx = {"ventas": Ventas.objects.all()}
    return render(request, 'aplicacion/ventas.html', ctx)

@login_required
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


#=================ABOUT ME===============================

@login_required
def about(request):
    ctx = {"about": About.objects.all()}
    return render(request, 'aplicacion/about.html', ctx)



#=================BUSCAR CODIGO===============================

@login_required
def buscarCodigo(request):
    return render(request, "aplicacion/buscarCodigo.html")

@login_required
def buscar2(request):
    if request.GET['codigo']:
        codigo = request.GET['codigo']
        articulos = Articulo.objects.filter(codigo__icontains=codigo)
        return render(request, 
                      "aplicacion/resultadosCodigo.html",
                      {"codigo": codigo, "articulos": articulos})
    return HttpResponse("No se ingresaron datos para realizar busqueda")

#=================BUSCAR PROVEEDOR===============================

@login_required
def buscarProveedor(request):
    return render(request, "aplicacion/buscarProveedor.html")

@login_required
def buscar3(request):
    if request.GET['cuit']:
        cuit = request.GET['cuit']
        proveedores = Proveedor.objects.filter(cuit__icontains=cuit)
        return render(request, 
                      "aplicacion/resultadosProveedor.html",
                      {"ciut": cuit, "proveedores": proveedores})
    return HttpResponse("No se ingresaron datos para realizar busqueda")

#=================BUSCAR VENDEDOR===============================

@login_required
def buscarVendedor(request):
    return render(request, "aplicacion/buscarVendedor.html")

@login_required
def buscar4(request):
    if request.GET['dni']:
        dni = request.GET['dni']
        vendedores = Vendedor.objects.filter(dni__icontains=dni)
        return render(request, 
                      "aplicacion/resultadosVendedores.html",
                      {"dni": dni, "vendedores": vendedores})
    return HttpResponse("No se ingresaron datos para realizar busqueda")

#=================BUSCAR VENTA===============================

@login_required
def buscarVenta(request):
    return render(request, "aplicacion/buscarVenta.html")

@login_required
def buscar5(request):
    if request.GET['codigo']:
        codigo = request.GET['codigo']
        ventas = Ventas.objects.filter(codigo__icontains=codigo)
        return render(request, 
                      "aplicacion/resultadosVentas.html",
                      {"codigo": codigo, "ventas": ventas})
    return HttpResponse("No se ingresaron datos para realizar busqueda")


#=========================CRUD======================(Creados con Class Based Views)
##=======================ARTICULOS
class ArticuloList(LoginRequiredMixin, ListView):
    model = Articulo
    
class ArticuloCreate(LoginRequiredMixin, CreateView):
    model = Articulo
    fields = ['codigo', 'nombre', 'marca']
    success_url = reverse_lazy('articulos')  

class ArticuloDetail(LoginRequiredMixin, DetailView):
    model = Articulo
    
class ArticuloUpdate(LoginRequiredMixin, UpdateView):
    model = Articulo
    fields = ['codigo', 'nombre', 'marca']
    success_url = reverse_lazy('articulos')  
    
class ArticuloDelete(LoginRequiredMixin, DeleteView):
    model = Articulo
    success_url = reverse_lazy('articulos')

##=======================VENDEDORES
class VendedorList(LoginRequiredMixin, ListView):
    model = Vendedor
    
class VendedorCreate(LoginRequiredMixin, CreateView):
    model = Vendedor
    fields = ['nombre', 'apellido', 'dni', 'telefono']
    success_url = reverse_lazy('vendedores')

class VendedorDetail(LoginRequiredMixin, DetailView):
    model = Vendedor

class VendedorUpdate(LoginRequiredMixin, UpdateView):
    model = Vendedor
    fields = ['nombre', 'apellido', 'dni', 'telefono']
    success_url = reverse_lazy('vendedores')

class VendedorDelete(LoginRequiredMixin, DeleteView):
    model = Vendedor
    success_url = reverse_lazy('vendedores')
    
##=======================PROVEEDORES    
class ProveedorList(LoginRequiredMixin, ListView):
    model = Proveedor

class ProveedorCreate(LoginRequiredMixin, CreateView):
    model = Proveedor
    fields = ['razonSocial', 'domicilio', 'cuit', 'email']
    success_url = reverse_lazy('proveedores')
    
class ProveedorDetail(LoginRequiredMixin, DetailView):
    model = Proveedor
    
class ProveedorUpdate(LoginRequiredMixin, UpdateView):
    model = Proveedor
    fields = ['razonSocial', 'domicilio', 'cuit', 'email']
    success_url = reverse_lazy('proveedores') 

class ProveedorDelete(LoginRequiredMixin, DeleteView):
    model = Proveedor
    success_url = reverse_lazy('proveedores')


##=======================VENTAS
class VentasList(LoginRequiredMixin, ListView):
    model = Ventas
    
class VentaCreate(LoginRequiredMixin, CreateView):
    model = Ventas
    fields = ['fecha', 'codigo', 'producto', 'cantidad']
    success_url = reverse_lazy('ventas')

class VentaDetail(LoginRequiredMixin, DetailView):
    model = Ventas
    
class VentaUpdate(LoginRequiredMixin, UpdateView):
    model = Ventas
    fields = ['fecha', 'codigo', 'producto', 'cantidad']
    success_url = reverse_lazy('ventas') 
    
class VentaDelete(LoginRequiredMixin, DeleteView):
    model = Ventas
    success_url = reverse_lazy('ventas')
    
#==================logIn====================

def login_request(request):
    if request.method == "POST":
        miForm = AuthenticationForm(request, request.POST)
        print(miForm)
        if miForm.is_valid():
            usuario = miForm.cleaned_data.get('username')
            clave = miForm.cleaned_data.get('password')
            user = authenticate(username=usuario, password=clave)
            if user is not None:
                login(request, user)
                try:
                    avatar = Avatar.objects.get(user=request.user.id).imagen.url
                except:
                    avatar = '/media/avatares/default.png'
                finally:
                    request.session['avatar'] = avatar
                
                return render(request, "aplicacion/base.html", {"mensaje": f"Bienvenido {usuario}"})
            else:
                 return render(request, "aplicacion/login.html", {"form":miForm, "mensaje": f"Datos Inválidos"})
        else:
            return render(request, "aplicacion/login.html", {"form":miForm, "mensaje": f"Datos Inválidos"})
    
    miForm = AuthenticationForm()
        
    return render(request, 'aplicacion/login.html', {"form":miForm})

#======================registro=========================

def register(request):
    if request.method == "POST":
        form = RegistroUsuariosForm(request.POST)
        if form.is_valid():
            usuario = form.cleaned_data.get('username')
            form.save()
            return render(request, "aplicacion/base.html", {"mensaje":"Usuario creado"})
    else:
        form = RegistroUsuariosForm()
        
    return render(request, 'aplicacion/registro.html', {"form":form})

#======================editar perfiles====================

@login_required
def editarPerfil(request):
    usuario = request.user
    if request.method == "POST":
        form = UserEditForm(request.POST)
        if form.is_valid():
            usuario.email = form.cleaned_data.get('email')
            usuario.password1 = form.cleaned_data.get('password1')
            usuario.password2 = form.cleaned_data.get('password2')
            usuario.first_name = form.cleaned_data.get('first_name')
            usuario.last_name = form.cleaned_data.get('last_name')
            usuario.save()
            return render(request, "aplicacion/base.html", {'mensaje': f"Usuario {usuario.username} actualizado correctamente"})
        else:
            return render(request, "aplicacion/editarPerfil.html", {'form': form})
    else:
        form = UserEditForm(instance=usuario)
    return render(request, "aplicacion/editarPerfil.html", {'form': form, 'usuario':usuario.username})
        
@login_required
def agregarAvatar(request):
    if request.method == "POST":
        form = AvatarFormulario(request.POST, request.FILES)
        if form.is_valid():
            u = User.objects.get(username=request.user)
            avatarViejo = Avatar.objects.filter(user=u)
            if len(avatarViejo) > 0:
                avatarViejo[0].delete()
            
            avatar = Avatar(user=u, imagen=form.cleaned_data['imagen'])
            avatar.save()    
            
            imagen = Avatar.objects.get(user=request.user.id).imagen.url
            request.session['avatar'] = imagen
           
            return render(request, "aplicacion/base.html")
    else:
        form = AvatarFormulario()
    return render(request, "aplicacion/agregarAvatar.html", {'form': form})