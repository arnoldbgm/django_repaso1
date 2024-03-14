from django.shortcuts import render
from django.views.generic import ListView
from .models import EmpleadosModel
from django.db.models.functions import Lower

class ListAllEmpleados(ListView):
    template_name = 'empleados/list_all.html'
    model = EmpleadosModel


class ListByAreaEmpleados(ListView):
    template_name = 'empleados/list_area.html'

    def get_queryset(self):
        parametroUrl = self.kwargs['shortname'].lower()  # Convertir a minúsculas
        queryset = EmpleadosModel.objects.annotate(lower_shortname=Lower('departamento__short_name')).filter(lower_shortname=parametroUrl)
        return queryset
