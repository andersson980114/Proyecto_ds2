from django.contrib import admin
from app.models import Usuario, Cliente, Mascota, Servicio, Historia

# Register your models here.
admin.site.register(Usuario)
admin.site.register(Cliente)
admin.site.register(Mascota)
admin.site.register(Servicio)
admin.site.register(Historia)