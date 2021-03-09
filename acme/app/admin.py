from django.contrib import admin 
from .models import Usuario

#4 importar y registrar modelos
#despues de crear el modelo diligenciar el forms
admin.site.register(Usuario)
