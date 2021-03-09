from django.urls import path
from .views import Index, ingreso,  RegistroUsuario

#2 se define una url para cada vew(las vews se debesn importar de .vews)
urlpatterns = [
    path('', Index, name="Index"), 
    path('RegistroUsuario/', RegistroUsuario, name= "RegistroUsuario"), 

]