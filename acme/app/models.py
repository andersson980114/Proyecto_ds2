from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager

# Create your models here.

#3 crear los modelos de las tablas de la base de datos
#despues de crear las tablas ejecutar el makemigrations y migrate en el terminal

opciones_cargo = [ 
    [1,"Veterinario"],
    [2,"Recepcionista"]
]

opciones_Sexo= [ 
    [1,"Macho"],
    [2,"Hembra"]
]
class UsuarioManager(BaseUserManager):
    def create_user(self, email, username, Nombres, password = None):
        if not email:
            raise ValueError('El usuario debe tener correo electronico')

        usuario = self.model(
            username = username, 
            email = self.normalize_email(email),
            Nombres = Nombres, )
        
        usuario.set_password(password)
        usuario.save()
        return usuario
    
    def create_superuser(self, email, username, Nombres,  password):
        usuario = self.create_user(
            username = username, 
            email = self.normalize_email(email),
            Nombres = Nombres, 
            password= password)
        
        usuario.usuario_administrador = True
        usuario.save()
        return usuario

class Usuario(AbstractBaseUser): 
    id = models.AutoField(primary_key=True)
    username  = models.CharField('Cedula', unique=True, max_length=20, blank=False, null=False)
    Nombres = models.CharField('Nombres',max_length=50, blank=False, null=False)
    Apellidos = models.CharField('Apellidos',max_length=50, blank=False, null=False)
    Telefono = models.CharField('Telefono',max_length=20, blank=False, null=False)
    Direccion = models.CharField('Direccion',max_length=50, blank=False, null=False)
    email = models.EmailField('Correo',max_length=50, blank=False, null=False)
    Cargo = models.IntegerField('Cargo',choices = opciones_cargo)
    usuario_activo = models.BooleanField(default=True)
    usuario_administrador = models.BooleanField(default=False)  
    objects = UsuarioManager()

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['email', 'Nombres', 'apellido']

    class Meta:
        verbose_name = 'Usuario'
        verbose_name_plural= 'Usuarios'
        ordering = ['Nombres'] #se ordena según el parametro indicado(ej: nombre, apellido o cedula)

    
    def _str_(self):
        return f'{self.Nombres},{self.Apellidos}'

    def has_perm(self, perm, obj = None):
        return True
    
    def has_module_perms(self, app_label):
        return True
    
    @property
    def is_staff(self):
        return self.usuario_administrador

class Servicio(models.Model):
    id = models.AutoField(primary_key=True)
    Codigo = models.CharField('Codigo',unique = True, max_length=50, blank=False, null=False)
    Nombre = models.CharField('Nombre',max_length=50, blank=False, null=False)
    Cantidad = models.IntegerField('Cantidad', blank=False, null=False)
    Valor = models.IntegerField('Valor', blank=False, null=False)

    class Meta:
        verbose_name = 'Servicio'
        verbose_name_plural= 'Servicios'
        ordering = ['Codigo'] #se ordena según el parametro indicado(ej: nombre, apellido o cedula)

    def _str_(self):
        return f'{self.Codigo},{self.Nombre}'
    
    
class Cliente(models.Model):
    id = models.AutoField(primary_key=True)
    Nombre = models.CharField('Nombre',max_length=50, blank=False, null=False)
    Apellido = models.CharField('Apellido',max_length=50, blank=False, null=False)
    Telefono = models.CharField('Telefono',max_length=20, blank=False, null=False)
    Direccion = models.CharField('Direccion',max_length=50, blank=False, null=False)
    Correo = models.EmailField('Correo',max_length=50, blank=False, null=False) 
    Cedula = models.CharField('Cedula',max_length=20, blank=False, null=False)
      
    class Meta:
        verbose_name = 'Cliente'
        verbose_name_plural= 'Clientes'
        ordering = ['Nombre'] #se ordena según el parametro indicado(ej: nombre, apellido o cedula)

    def __str__(self):
        return f'{self.Cedula}: {self.Nombre}'

class Mascota(models.Model):
    id = models.AutoField(primary_key=True)
    Nombre = models.CharField('Nombre',max_length=20, blank=False, null=False)
    Especie = models.CharField('Especie',max_length=20, blank=False, null=False)
    Raza = models.CharField('Raza',max_length=20, blank=False, null=False)
    Fecha_nacimiento = models.DateField('Fecha de Nacimiento', blank=False, null=False)
    Sexo = models.IntegerField('Sexo', choices = opciones_Sexo)  
    Cliente_id = models.ForeignKey(Cliente, on_delete = models.CASCADE)
      
    class Meta:
        verbose_name = 'Mascota'
        verbose_name_plural= 'Mascotas'
        ordering = ['Nombre'] #se ordena según el parametro indicado(ej: nombre, apellido o cedula)

    def _str_(self):
        return self.Nombre


class Historia(models.Model):
    id = models.AutoField(primary_key=True)
    Fecha_creacion = models.DateField('Fecha de Creación', blank=False, null=False)
    Mascota_id = models.ForeignKey(Mascota, on_delete = models.CASCADE)

    class Meta:
        verbose_name = 'Historia'
        verbose_name_plural= 'Historias'
        ordering = ['id'] #se ordena según el parametro indicado(ej: nombre, apellido o cedula)

    def _str_(self):
        return f'{self.id}'

class EntradaHistoria(models.Model):
    id = models.AutoField(primary_key=True)
    Historia_id = models.ForeignKey(Historia, on_delete = models.CASCADE)
    Veterinario = models.CharField('Veterinario',max_length=50, blank=False, null=False)
    Fecha = models.DateTimeField('Fecha' ,blank=False, null=False)
    Observaciones = models.CharField('Observaciones',max_length=500, blank=False, null=False)
    Tipo = models.CharField('Tipo',max_length=50, blank=False, null=False)

    class Meta:
        verbose_name = 'EntradaHistoria'
        verbose_name_plural= 'EntradasHistorias'
        ordering = ['id'] #se ordena según el parametro indicado(ej: nombre, apellido o cedula)

    def _str_(self):
        return f'{self.id}'
    
  