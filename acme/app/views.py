from django.shortcuts import render, redirect
from .forms import UsuarioForm
from django.contrib import messages
from django.contrib.auth import authenticate, login
# Create your views here.
#1 crear vews 

def Index(request):
    return render(request, 'app/Index.html')

def ingreso(request):
    return render(request, 'app/ingreso.html')


def RegistroUsuario(request):
    data = {
        'form' : UsuarioForm()
    }

    if request.method == 'POST':
        formulario = UsuarioForm(data = request.POST)
        if formulario.is_valid():
            formulario.save() 
            messages.success(request, "Usuario registrado")
            return redirect(to=RegistroUsuario)
        else:
             messages.success(request, "Ha ocurrido un error. Intentelo de nuevo")

    return render(request, 'registration/RegistroUsuario.html', data)


 