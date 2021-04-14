from django.urls import path
from django.views.i18n import JavaScriptCatalog
<<<<<<< HEAD
from .views import Index, RegistroCliente, RegistroUsuario, RegistroMascota, BuscarUsuario, ModificarUsuario, EliminarUsuario, ListarClientes, RegistroServicio, BuscarServicio ,ModificarServicio, EliminarServicio, RegistrarHistorial, ConsultarHistorial, RegistrarEntrada, VerHistorial, Detalles
=======
from .views import Index, RegistroCliente, RegistroUsuario, RegistroMascota, BuscarUsuario, ModificarUsuario, EliminarUsuario, ListarClientes, RegistroServicio, BuscarServicio ,ModificarServicio, EliminarServicio, RegistrarHistorial, ConsultarHistorial, RegistrarEntrada
>>>>>>> f6165acb6fcb9aa3836da787fe1db54b30dbd95c
#2 se define una url para cada vew(las vews se debesn importar de .vews)
urlpatterns = [
    path('', Index, name="Index"), 
    path('jsi18n', JavaScriptCatalog.as_view(), name= 'js-catlog'),
    path('RegistroUsuario', RegistroUsuario, name= "RegistroUsuario"), 
    path('RegistroServicio', RegistroServicio, name= "RegistroServicio"),
    path('RegistroCliente', RegistroCliente, name = "RegistroCliente"), 
    path('RegistroMascota/<int:id>/', RegistroMascota, name= "RegistroMascota"), 
    path('BuscarUsuario', BuscarUsuario, name= "BuscarUsuario"), 
    path('ListarClientes', ListarClientes, name= "ListarClientes"),  
    path('ModificarUsuario/<id>/', ModificarUsuario, name= "ModificarUsuario"), 
    path('EliminarUsuario/<id>/', EliminarUsuario, name= "EliminarUsuario"), 
    path('BuscarServicio', BuscarServicio, name= "BuscarServicio"), 
    path('ModificarServicio/<id>/', ModificarServicio, name= "ModificarServicio"), 
    path('EliminarServicio/<id>/', EliminarServicio, name= "EliminarServicio"), 
    path('RegistrarHistorial', RegistrarHistorial, name= "RegistrarHistorial"),
    path('ConsultarHistorial', ConsultarHistorial, name= "ConsultarHistorial"), 
    path('RegistrarEntrada', RegistrarEntrada, name= "RegistrarEntrada"), 
    path('VerHistorial/<id>/', VerHistorial, name= "VerHistorial"), 
    path('Detalles/<id>/', Detalles, name= "Detalles"), 
    
]
