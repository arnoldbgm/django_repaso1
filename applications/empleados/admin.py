from django.contrib import admin
from .models import EmpleadosModel, HabilidadesModel


admin.site.register(HabilidadesModel)

# Personalizaremos el admin de DJANGO


class EmpleadoAdmin(admin.ModelAdmin):
    list_display = (
        'first_name',
        'last_name',
        'job',
        'full_name'
    )

    def full_name(self, obj):
        return 'Nombre' + ' '+ obj.first_name + ' ' + obj.last_name

    list_filter = ('job',)


admin.site.register(EmpleadosModel, EmpleadoAdmin)
