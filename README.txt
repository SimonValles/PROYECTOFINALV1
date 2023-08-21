Autor: Simon Valles
Titulo: Proyecto Final


Objetivo del trabajo practico entregado:

Este programa consiste en el diseño de una pagina web para una tienda en la cual se puede administrar el ingreso de información:

-Articulos
-Ventas
-Vendedores  
-Proveedores


La información se visualiza en forma de tablas.

Cada función operacionalizada a traves de botones en la cabecera permite visualizar los registros guardados en la base de datos.

Como una opción adicional en la pagina de inicio se pueden Buscar: ARTICULOS, VENDEDORES, PROVEEDORES y VENTAS, presionando el boton buscar, para lo cual
se debe conocer el dato a ingresar. Si no lo conoce, puede entrar a cabecera en cualquier seccion, anotar el dato solicitado y consultarlo en la pagina de inicio.

Todas las funciones del programa pueden ser utilizadas si y solo si el usuario se encuentra loggeado.

Para hacer mas agradable la interfaz, cada usuario podrá cargar su avatar preferido en formato .png

 

------------------------------------------------------------------------------------------------------
                    ¿COMO EJECUTAMOS EL PROGRAMA?

Direccion url para accesar a la pagina de inicio http://127.0.0.1:8000/aplicacion/

Datos de super usuario para acceder al programa:

"ADMIN"
Nombre de usuario = admin1
Contraseña = admin


Los datos de los usuarios se pueden modificar desde admin y desde el boton en la cabecera. Lo mismo para agregar tu avatar o modificarlo.

Como funcionalidades tenemos las siguientes aplicaciones:

1) si no estas logeado solo puedes ver la pagina de inicio y los botones:

-Inicio
-Registrarse
-Login

2) una vez loggeado el usuario tendrá acceso a toda la información tanto por accesos en pagina de inicio como por botones en cabecera:

-Inicio = te devuelve a la pagina de inicio
-Articulos = creacion, visualizacion, modificacion y eliminacion de registros
-Ventas = creacion, visualizacion, modificacion y eliminacion de registros
-Vendedores = creacion, visualizacion, modificacion y eliminacion de registros   
-Proveedores= creacion, visualizacion, modificacion y eliminacion de registros
-Acerca de mi = una pagina referencia que muestra cierta información del creador del programa.
-Administracion = Acceso a sitio administrativo Django
-Editar perfil
-Agregar avatar
-Login = puedes loggearte, y una vez logeado, habilita el boton logout.

Cada boton redirecciona a una pagina que muestra los datos almacenados en nuestra base de datos.

-La carga de datos tambien se puede hacer por DB Browser y Administracion.

--------------------------------------------------------------------------------------------------------