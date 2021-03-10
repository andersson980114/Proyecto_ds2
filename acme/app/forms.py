from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import Usuario

#forms.ModelForm = no ineractua con el sistema(cliente, mascota, productos)
#UserCreationForm = interactua con el sistema(veterinario, recepcionista)
class UsuarioForm(UserCreationForm):
    class Meta:
        model = Usuario
                 #Datos con los que se llenara el formulario (atributos de la tabla sin el ID)
        fields = ['Nombre', 'Apellido', 'Telefono', 'Direccion', 'Correo', 'Cargo', 'Estado', 'Cedula', 'Contraseña']
        
         
        widgets = {
            'Nombre': forms.TextInput(
                attrs = {'class': 'form.control', 'placeholder': 'Ingrese el Nombre' } ),
            'Apellido': forms.TextInput(
                attrs = {  'class': 'form.control', 'placeholder': 'Ingrese el Apellido' }),
            'Telefono': forms.TextInput(
                attrs = { 'class': 'form.control',  'placeholder': 'Ingrese el Telefono' }),
            'Direccion': forms.TextInput(
                attrs = {'class': 'form.control', 'placeholder': 'Ingrese el Direccion' }),
            'Correo': forms.EmailInput(
                attrs = { 'class': 'form.control', 'placeholder': 'Ingrese el Correo' }),
            'Cargo': forms.Select(
                attrs = {  'class': 'form.control', 'placeholder': 'Elija el Cargo' }),
            'Estado': forms.Select(
                attrs = { 'class': 'form.control', 'placeholder': 'Elija el Estado'}),
            'Cedula': forms.TextInput(
                attrs = { 'class': 'form.control', 'placeholder': 'Ingrese la Cedula' }),
            'Contraseña': forms.TextInput(
                attrs = { 'class': 'form.control', 'type':'Password' ,'placeholder': 'Ingrese el Contraseña' })}
     
    
        
 