from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse_lazy
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm
from django.views.generic import CreateView, ListView, UpdateView, DeleteView
from django.contrib.auth import authenticate, login
from .models import Usuario, Cliente, Mascota, Servicio , Historia, EntradaHistoria
from .forms import UsuarioForm, ClienteForm, MascotaForm, ServicioForm, HistoriaForm, EntradaHistoriaForm, FacturaForm, DetalleForm
from django.contrib.auth.models import User 
from django.contrib.auth.decorators import login_required
from django.db.models import Q

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
            return redirect('app:RegistroCliente')
        else:
             messages.success(request, "Ha ocurrido un error. Intentelo de nuevo")

    return render(request, 'app/RegistroCliente.html', data)

@login_required
def ListarClientes(request):
    queryset = request.GET.get("Buscar")
    clientes = Cliente.objects.all()

    if queryset:
        clientes = Cliente.objects.filter(
            Q(Cedula = queryset)
        ).distinct()
     
    data = {
        'clientes':clientes
    }
    return render(request, 'app/ListarClientes.html', data)

@login_required
def RegistroMascota(request, id): 
    cliente = Cliente.objects.get(pk=id)
    data = {
        'form' : MascotaForm(),
        'cliente':cliente
    }
    if request.method == 'POST':
        try:
            nombre = request.POST['nombre']
            especie = request.POST['especie']
            raza = request.POST['raza']
            fecha = request.POST['fecha']
            sexo = int(request.POST['sexo'])
            mascota = Mascota.objects.get_or_create(Nombre=nombre,Especie=especie,Raza=raza,Fecha_nacimiento=fecha,Sexo=sexo,Cliente_id=cliente)
            
            return redirect('app:RegistroMascota')
        except :
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
            if cargo == 1:
                
                user = User.objects.create_superuser(username=user,password=p1,email=email,first_name=name,last_name=last_name)
                
            else:
                user = User.objects.create_user(username=user,password=p1,email=email,first_name=name,last_name=last_name)
            user.save()
            form_class.save()   
            return redirect('app:RegistroUsuario')
        return render(request,'registration/RegistroUsuario.html',data) 

@login_required
def BuscarUsuario(request):
    usuarios = Usuario.objects.all()
    data = {
        'usuarios':usuarios
    }
    return render(request,'app/BuscarUsuario.html', data) 

@login_required
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
            return redirect( "app:BuscarUsuario")
        data["form"]= formulario 
              
    return render(request, 'app/ModificarUsuario.html', data)

@login_required
def EliminarUsuario(request, id):
    usuario = get_object_or_404(Usuario, id = id)
    usuario.delete()
    messages.success(request, "Usuario Eliminado correctamente")
    return redirect( "app:BuscarUsuario")

@login_required 
def RegistroServicio(request):
    data = {
        'form' : ServicioForm()
    }

    if request.method == 'POST':
        formulario = ServicioForm(data = request.POST)
        if formulario.is_valid():
            formulario.save() 
            messages.success(request, "Servicio Agregado")
            return redirect('app:RegistroServicio')
        else:
            messages.success(request, "Ha ocurrido un error. Intentelo de nuevo")
    return render(request, 'app/RegistroServicio.html', data)

@login_required
def BuscarServicio(request):

    queryset = request.GET.get("Buscar")
    servicios = Servicio.objects.all()

    if queryset:
        servicios = Servicio.objects.filter(
            Q(Codigo = queryset) |
            Q(Nombre = queryset)
        ).distinct()
    data = {
        'servicios':servicios
    }
    return render(request,'app/BuscarServicio.html', data) 
    

@login_required
def ModificarServicio(request, id):
    servicio = get_object_or_404(Servicio, id = id)
    data = {
        'form' : ServicioForm(instance = servicio)
    }

    if request.method == 'POST':
        formulario = ServicioForm(data = request.POST, instance = servicio, files =request.FILES)
        if formulario.is_valid():
            formulario.save()
            messages.success(request, "Servicio modificado correctamente")
            return redirect("app:BuscarServicio")
        data["form"]= formulario 
              
    return render(request, 'app/ModificarServicio.html', data)

@login_required
def EliminarServicio(request, id):
    servicio = get_object_or_404(Servicio, id = id)
    servicio.delete()
    messages.success(request, "Servicio Eliminado correctamente")
    return redirect("app:BuscarServicio")


@login_required
def RegistrarHistorial(request):
    data = {
        'form' : HistoriaForm()
    } 

    if request.method == 'POST':
        formulario = HistoriaForm(data = request.POST)
        if formulario.is_valid():
            formulario.save() 
            messages.success(request, "Historia clínica registrada")
            return redirect('app:RegistrarHistorial')
        else:
            messages.success(request, "Ha ocurrido un error. Intentelo de nuevo")

    return render(request, 'app/RegistrarHistorial.html', data)

@login_required
def ConsultarHistorial(request):
    queryset = request.GET.get("Buscar")
    historias = Historia.objects.all() 
    #cliente = Historia.objects.all().filter( type= Cliente.objects.get(Cedula=queryset))
    if queryset:
        historias = Historia.objects.filter(
            Q(Mascota_id__Cliente_id__Cedula = queryset)|
            Q(Mascota_id__Cliente_id__Nombre = queryset)|
            Q(Mascota_id__Cliente_id__Apellido = queryset)|
            Q(Mascota_id__Nombre = queryset)
        ).distinct()
    data = {
        'historias':historias
    }
    return render(request,'app/ConsultarHistorial.html', data) 

#@login_required
def VerHistorial(request, id):

    entradas = EntradaHistoria.objects.filter( Historia_id = id )

    data = {
        'entradas': entradas
    }
    return render(request,'app/VerHistorial.html', data) 



@login_required
def RegistrarEntrada(request): 
    data = {
        'form' : EntradaHistoriaForm()
    } 

    if request.method == 'POST':
        formulario = EntradaHistoriaForm(data = request.POST)
        if formulario.is_valid():
            formulario.save() 
            messages.success(request, "Entrada registrada")
            return redirect('app:RegistrarEntrada')
        else:
            messages.success(request, "Ha ocurrido un error. Intentelo de nuevo")

    return render(request, 'app/RegistrarEntrada.html', data)

@login_required
def Detalles(request, id): 
    entrada = get_object_or_404(EntradaHistoria, id = id)
    data = {
        'form' : EntradaHistoriaForm(instance = entrada )
    } 

    if request.method == 'POST':
        formulario = EntradaHistoriaForm(data = request.POST, isinstance =  entrada, files = request.FILES)
        data['form']= formulario

    return render(request, 'app/Detalles.html', data)

@login_required
def RegistrarFactura(request):
    data = {
        'form' : FacturaForm()
    } 

    if request.method == 'POST':
        formulario = FacturaForm(data = request.POST)
        if formulario.is_valid():
            formulario.save() 
            messages.success(request, "Factura registrada")
            return redirect('app:RegistrarFactura')
        else:
            messages.success(request, "Ha ocurrido un error. Intentelo de nuevo")

    return render(request, 'app/RegistrarFactura.html', data)

@login_required
def RegistrarDetalle(request):
    data = {
        'form' : DetalleForm()
    } 

    if request.method == 'POST':
        formulario = DetalleForm(data = request.POST)
        if formulario.is_valid():
            formulario.save() 
            messages.success(request, "Detalle registrada")
            return redirect('app:RegistrarDetalle')
        else:
            messages.success(request, "Ha ocurrido un error. Intentelo de nuevo")

    return render(request, 'app/RegistrarDetalle.html', data)

    


