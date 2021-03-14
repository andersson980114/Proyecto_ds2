from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse_lazy
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm
from django.views.generic import CreateView, ListView, UpdateView, DeleteView
from django.contrib.auth import authenticate, login
from .models import Usuario, Cliente
from .forms import UsuarioForm, ClienteForm, MascotaForm
from django.contrib.auth.models import User 
from django.contrib.auth.decorators import login_required

# Create your views here.
#1 crear vews 

def Index(request):
    if  request.user.is_authenticated:
        usuario = request.user.username
    else:
        usuario = None
    if usuario:
        try:
            usuario_db = Usuario.objects.get(username=usuario)
            cargo = usuario_db.Cargo
        except :
            cargo = 'Admin'
    else:
        cargo=None
    context = {
            'type':cargo
            }
    return render(request, 'app/Index.html',context)


@login_required
def RegistroCliente(request):
    data = {
        'form' : ClienteForm()
    }

    if request.method == 'POST':
        formulario = ClienteForm(data = request.POST)
        if formulario.is_valid():
            formulario.save() 
            messages.success(request, "Cliente registrado")
            return redirect(to=RegistroCliente)
        else:
             messages.success(request, "Ha ocurrido un error. Intentelo de nuevo")

    return render(request, 'app/RegistroCliente.html', data)


def RegistroMascota(request):
    data = {
        'form' : MascotaForm()
    }

    if request.method == 'POST':
        formulario = MascotaForm(data = request.POST)
        if formulario.is_valid():
            formulario.save() 
            messages.success(request, "Mascota registrada")
            return redirect(to=RegistroMascota)
        else:
            messages.success(request, "Ha ocurrido un error. Intentelo de nuevo")

    return render(request, 'app/RegistroMascota.html', data)

 
@login_required
def RegistroUsuario(request):
    form_class = UsuarioForm()
    data = {
            'form':form_class,
            }

    if request.method == 'GET':
        return render(request,'registration/RegistroUsuario.html',data)
    else:
        form_class = UsuarioForm(request.POST)
        if form_class.is_valid():
            user = request.POST['username']
            p1 = request.POST['password']
            email = request.POST['email']
            name = request.POST['Nombres']
            last_name = request.POST['Apellidos']
            cargo = int(request.POST['Cargo'])
            user = User.objects.create_user(username=user,password=p1,email=email,first_name=name,last_name=last_name)
            user.save()
            form_class.save()   
            return redirect(to=RegistroUsuario)
        return render(request,'registration/RegistroUsuario.html',data) 


def BuscarUsuario(request):
    usuarios = Usuario.objects.all()
    data = {
        'usuarios':usuarios
    }
    return render(request,'app/BuscarUsuario.html', data) 

def ModificarUsuario(request, id):
    
    usuario = get_object_or_404(Usuario, id = id)

    data = {
        'form' : UsuarioForm(instance = usuario)
    }

    if request.method == 'POST':
        formulario = UsuarioForm(data = request.POST, instance = usuario, files =request.FILES)
        if formulario.is_valid():
            formulario.save()
            messages.success(request, "Usuario modificado correctamente")
            return redirect(to = "BuscarUsuario")
        data["form"]= formulario 
              
    return render(request, 'app/ModificarUsuario.html', data)

def EliminarUsuario(request, id):
    usuario = get_object_or_404(Usuario, id = id)
    usuario.delete()
    messages.success(request, "Usuario Eliminado correctamente")
    return redirect(to = "BuscarUsuario")
