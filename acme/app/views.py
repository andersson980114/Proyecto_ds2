from django.shortcuts import render 
from .forms import UsuarioForm
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
            data["mensaje"] = "Usuario Guardado"
        else:
            data["form"]= formulario

    return render(request, 'app/RegistroUsuario.html', data)


 