from django.db import models

# Create your models here.
#3 crear los modelos de las tablas de la base de datos
#despues de crear las tablas ejecutar el makemigrations y migrate en el terminal

opciones_activo = [
    [1, "Activo"],
    [2, "Inactivo"]
]
opciones_cargo = [
    [1,"Veterinario"],
    [2,"Recepcionista"]
]

class Usuario(models.Model):
    id = models.AutoField(primary_key=True)
    Nombre = models.CharField(max_length=20, blank=False, null=False)
    Apellido = models.CharField(max_length=20, blank=False, null=False)
    Telefono = models.CharField(max_length=20, blank=False, null=False)
    Direccion = models.CharField(max_length=50, blank=False, null=False)
    Correo = models.EmailField(max_length=50, blank=False, null=False)
    Cargo = models.IntegerField(choices = opciones_cargo)
    Estado = models.IntegerField(choices = opciones_activo)
    Cedula = models.CharField(max_length=20, blank=False, null=False)
    Contraseña = models.CharField(max_length=20, blank=False, null=False)

    class Meta:
        verbose_name = 'Usuario'
        verbose_name_plural= 'Usuarios'
        ordering = ['Nombre'] #se ordena según el parametro indicado(ej: nombre, apellido o cedula)

    def _str_(self):
        return self.Nombre