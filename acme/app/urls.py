from django.urls import path
from .views import Index, RegistroCliente, RegistroUsuario, RegistroMascota, BuscarUsuario
#2 se define una url para cada vew(las vews se debesn importar de .vews)
urlpatterns = [
    path('', Index, name="Index"), 
    path('RegistroCliente', RegistroCliente, name = "RegistroCliente"),
    path('RegistroUsuario', RegistroUsuario, name= "RegistroUsuario"), 
    path('RegistroMascota', RegistroMascota, name= "RegistroMascota"), 
    path('BuscarUsuario', BuscarUsuario, name= "BuscarUsuario"), 
 
]
