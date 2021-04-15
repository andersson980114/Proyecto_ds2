from django.contrib import admin
from app.models import Usuario, Cliente, Mascota, Servicio, Historia, EntradaHistoria, Factura

# Register your models here.

class MascotaAdmin(admin.ModelAdmin):
    search_fields = ('id'), ('Nombre'), ('Cliente_id__Nombre')
    ordering = ['id']


class HistoriaAdmin(admin.ModelAdmin):
    autocomplete_fields = ['Mascota_id']
    search_fields=('Mascota_id__Cliente_id__Cedula'), ('Mascota_id__Nombre')
    ordering = ['id']

class EntradaHistoriaAdmin(admin.ModelAdmin):
    autocomplete_fields = ['Historia_id']
    ordering = ['Historia_id']



admin.site.register(Usuario)
admin.site.register(Cliente)
admin.site.register(Mascota,  MascotaAdmin)
admin.site.register(Servicio)
admin.site.register(Historia, HistoriaAdmin)
admin.site.register(EntradaHistoria, EntradaHistoriaAdmin)
admin.site.register(Factura)