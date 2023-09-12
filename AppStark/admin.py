from django.contrib import admin
from .models import *

class ServiciosAdmin(admin.ModelAdmin):
    list_display = ['Nombre_Servicio','Tipo_Servicio', 'ID_Servicio']

admin.site.register(Lista_Clientes)
admin.site.register(Servicios, ServiciosAdmin)
admin.site.register(Contratacion)
# Register your models here.
