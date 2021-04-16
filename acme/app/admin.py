from django.contrib import admin
from app.models import Usuario, Cliente, Mascota, Servicio, Historia, EntradaHistoria, Factura, DetalleFactura

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

class ClienteAdmin(admin.ModelAdmin):
    search_fields = ('Cedula'), ('Nombre')
    ordering = ['Cedula']

class FacturaAdmin(admin.ModelAdmin):
    autocomplete_fields = ['Cliente_id']
    ordering = ['Cliente_id']

class ServicioAdmin(admin.ModelAdmin):
    search_fields = ('id'), ('Nombre')
    ordering = ['id']

class DetalleFacturaAdmin(admin.ModelAdmin):
    autocomplete_fields = ['Servicio_id']
    ordering = ['Servicio_id']



admin.site.register(Usuario)
admin.site.register(Cliente, ClienteAdmin)
admin.site.register(Mascota,  MascotaAdmin)
admin.site.register(Servicio, ServicioAdmin)
admin.site.register(Historia, HistoriaAdmin)
admin.site.register(EntradaHistoria, EntradaHistoriaAdmin)
admin.site.register(Factura, FacturaAdmin)
admin.site.register(DetalleFactura, DetalleFacturaAdmin)