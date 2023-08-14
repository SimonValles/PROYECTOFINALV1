from django import forms

class ArticuloForm(forms.Form):
    codigo = forms.CharField(label='Código del Artículo', max_length=50, required=True)
    nombre = forms.CharField(label='Nombre',max_length=50, required=True)
    marca = forms.CharField(label='Marca', max_length=50, required=True)
    
class VendedorForm(forms.Form):
    nombre = forms.CharField(label='Nombre del Vendedor', max_length=50, required=True)
    apellido = forms.CharField(label='Apellido del Vendedor', max_length=50, required=True)
    dni = forms.CharField(label='DNI', max_length=15, required=True)
    telefono = forms.CharField(label='Telefono', max_length=20, required=True)
    
class ProveedorForm(forms.Form):
    razonSocial = forms.CharField(label='Razon Social', max_length=50, required=True)
    domicilio = forms.CharField(label='Domicilio Fiscal', max_length=50, required=True)
    cuit = forms.CharField(label='CUIT', max_length=50, required=True)
    email = forms.EmailField(label='Email', required=False)
    
class VentasForm(forms.Form):
    fecha = forms.DateField(label='Fecha de Venta', required=True)
    codigo = forms.CharField(label='Codigo del Articulo', max_length=50, required=True)
    producto = forms.CharField(label='Nombre del Articulo', max_length=50, required=True)
    cantidad = forms.IntegerField(label='Unidades Vendidas', required=True)