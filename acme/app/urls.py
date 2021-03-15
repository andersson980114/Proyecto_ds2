from django.urls import path
from .views import Index, RegistroCliente, RegistroUsuario, RegistroMascota, BuscarUsuario, ModificarUsuario, EliminarUsuario, ListarClientes, RegistroServicio, BuscarServicio ,ModificarServicio, EliminarServicio
#2 se define una url para cada vew(las vews se debesn importar de .vews)
urlpatterns = [
    path('', Index, name="Index"), 
    path('RegistroUsuario', RegistroUsuario, name= "RegistroUsuario"), 
    path('RegistroServicio', RegistroServicio, name= "RegistroServicio"),
    path('RegistroCliente', RegistroCliente, name = "RegistroCliente"), 
    path('RegistroMascota', RegistroMascota, name= "RegistroMascota"), 
    path('BuscarUsuario', BuscarUsuario, name= "BuscarUsuario"), 
    path('ListarClientes', ListarClientes, name= "ListarClientes"),  
    path('ModificarUsuario/<id>/', ModificarUsuario, name= "ModificarUsuario"), 
    path('EliminarUsuario/<id>/', EliminarUsuario, name= "EliminarUsuario"), 
    path('BuscarServicio', BuscarServicio, name= "BuscarServicio"), 
    path('ModificarServicio/<id>/', ModificarServicio, name= "ModificarServicio"), 
    path('EliminarServicio/<id>/', EliminarServicio, name= "EliminarServicio"), 

]
