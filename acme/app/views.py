from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm
from django.views.generic import CreateView, ListView, UpdateView, DeleteView
from django.contrib.auth import authenticate, login
from .models import Usuario, Cliente
from .forms import UsuarioForm, ClienteForm
from django.contrib.auth.models import User 
from django.contrib.auth.decorators import login_required

# Create your views here.
#1 crear vews 

def Index(request):
    return render(request, 'app/Index.html')

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

@login_required
def RegistroUsuario(request):
    form_class = UsuarioForm()
    context = {
            'form':form_class,
            }

    if request.method == 'GET':
        return render(request,'registration/RegistroUsuario.html',context)
    else:
        form_class = UsuarioForm(request.POST)
        if form_class.is_valid():
            user = request.POST['username']
            p1 = request.POST['password']
            email = request.POST['email']
            name = request.POST['Nombres']
            last_name = request.POST['Apellidos']
            user = User.objects.create_user(username=user,password=p1,email=email,first_name=name,last_name=last_name)
            user.save()
            form_class.save()
            return redirect('/')
        return render(request,'registration/RegistroUsuario.html',context) 
