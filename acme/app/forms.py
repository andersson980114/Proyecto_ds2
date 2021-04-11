from django import forms

from django.contrib.admin.widgets import AutocompleteSelect, AdminDateWidget
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.forms import UserCreationForm
from .models import Usuario, Cliente, Mascota, Servicio, Historia, EntradaHistoria

class UsuarioForm(forms.ModelForm): 

    password = forms.CharField(label = 'Conraseña', widget = forms.PasswordInput(
        attrs = {'class': 'form.control', 'type':'Password' ,'placeholder': 'Ingrese el Contraseña' }
    ))

    class Meta:
        model = Usuario
                 #Datos con los que se llenara el formulario (atributos de la tabla sin el ID)
        fields = ['Nombres', 'Apellidos', 'Telefono', 'Direccion', 'email', 'Cargo', 'username', 'password']
         
        widgets = {
            'Nombres': forms.TextInput(
                attrs = {'class': 'form.control', 'placeholder': 'Ingrese el Nombre' }),
            'Apellidos': forms.TextInput(
                attrs = {  'class': 'form.control', 'placeholder': 'Ingrese el Apellido' }),
            'Telefono': forms.TextInput(
                attrs = { 'class': 'form.control',  'placeholder': 'Ingrese el Telefono' }),
            'Direccion': forms.TextInput(
                attrs = {'class': 'form.control', 'placeholder': 'Ingrese el Direccion' }),
            'email': forms.EmailInput(
                attrs = { 'class': 'form.control', 'placeholder': 'Ingrese el Correo' }),
            'Cargo': forms.Select(
                attrs = {  'class': 'form.control', 'placeholder': 'Elija el Cargo' }), 
            'username': forms.TextInput(
                attrs = { 'class': 'form.control', 'placeholder': 'Ingrese la Cedula' }),
        }

class loginForm(AuthenticationForm): 
    def __init__(self, *args, **kwargs):
        super(loginForm, self).__init__(*args, **kwargs)

    Cedula = forms.CharField(widget = forms.TextInput(attrs={
        'class': 'form.control',
        'type' : 'text',
        'placeholder': 'Ingrese la Cedula',
        })) 
    
    Contraseña = forms.CharField(widget = forms.TextInput(attrs={
        'class': 'form.control',
        'type' : 'password',
        'placeholder': 'Ingrese la Contraseña',
        })) 

##CLiente
class ClienteForm(forms.ModelForm): 
 
    class Meta:
        model = Cliente
                 #Datos con los que se llenara el formulario (atributos de la tabla sin el ID)
        fields = ['Nombre', 'Apellido', 'Telefono', 'Direccion',  'Correo', 'Cedula']
         
        widgets = {
            'Nombre': forms.TextInput(
                attrs = {'class': 'form.control', 'placeholder': 'Ingrese el Nombre del Cliente' }),
            'Apellido': forms.TextInput(
                attrs = {  'class': 'form.control', 'placeholder': 'Ingrese el Apellido del Cliente' }),
            'Telefono': forms.TextInput(
                attrs = { 'class': 'form.control',  'placeholder': 'Ingrese el Telefono del Cliente' }),
            'Direccion': forms.TextInput(
                attrs = {'class': 'form.control', 'placeholder': 'Ingrese el Direccion del Cliente' }),
            'Correo': forms.EmailInput(
                attrs = { 'class': 'form.control', 'placeholder': 'Ingrese el Correo del Cliente' }), 
            'Cedula': forms.TextInput(
                attrs = { 'class': 'form.control', 'placeholder': 'Ingrese la Cedula del Cliente' })
        }



class MascotaForm(forms.Form):   
    nombre = forms.CharField(max_length=20,label='Nombre de la mascota')
    especie = forms.CharField(max_length=20,label='Especie')
    raza = forms.CharField(max_length=20,label='Raza') 
    fecha = forms.DateField(widget=AdminDateWidget())
    sexo = forms.ChoiceField(choices=[(1,'Macho'),(2,'Hembra')])
    


class ServicioForm(forms.ModelForm):   
    class Meta:
        model = Servicio
                 #Datos con los que se llenara el formulario (atributos de la tabla sin el ID)
        fields = ['Codigo', 'Nombre', 'Cantidad', 'Valor']
        widgets = {
            'Codigo': forms.TextInput(
                attrs = {'class': 'form.control', 'placeholder': 'Ingrese el Codigo del Producto' }),
            'Nombre': forms.TextInput(
                attrs = {  'class': 'form.control', 'placeholder': 'Ingrese el Nombre ' }),
            'Cantidad': forms.NumberInput(
                attrs = { 'class': 'form.control',  'placeholder': 'Ingrese la Cantidad' }),
            'Valor': forms.NumberInput( 
                attrs = {'class': 'form.control', 'placeholder': 'Ingrese el Valor' }) #llave foranea
        }

class HistoriaForm(forms.ModelForm):   
    class Meta:
        model = Historia
                 #Datos con los que se llenara el formulario (atributos de la tabla sin el ID)
        fields = ['Mascota_id', 'Fecha_creacion']
        widgets = {
            'Fecha_creacion': forms.SelectDateWidget( 
                attrs = {'class': 'form.control', 'placeholder': 'Ingrese la fecha de creación' }),
           
            'Mascota_id': forms.Select(
                attrs = { 'class': 'form.control', 'placeholder': 'Ingrese la mascota' })#llave foranea
        }

class EntradaHistoriaForm(forms.ModelForm):   
    class Meta:
        model = EntradaHistoria
                 #Datos con los que se llenara el formulario (atributos de la tabla sin el ID)
        fields = ['Historia_id', 'Veterinario', 'Fecha', 'Observaciones', 'Tipo']
        widgets = {

            'Historia_id': forms.Select(
                attrs = { 'class': 'form.control', 'placeholder': 'Ingrese la historia clínica' }),#llave foranea
           
            'Veterinario': forms.TextInput(
                attrs = {  'class': 'form.control', 'placeholder': 'Ingrese el veterinario' }),           

            'Fecha': forms.SelectDateWidget( 
                attrs = {'class': 'form.control', 'placeholder': 'Ingrese la fecha de entrada' }),
        
            'Observaciones': forms.TextInput(
                attrs = {  'class': 'form.control', 'placeholder': 'Ingrese las observaciones' }),
            
            'Tipo': forms.TextInput(
                attrs = {  'class': 'form.control', 'placeholder': 'Ingrese el tipo de la entrada' })
        }
    
