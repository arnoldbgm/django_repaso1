from django.shortcuts import render
from django.views.generic import TemplateView, ListView
from .models import Prueba

#El templeateView ya me permite visualizar una HTML

# class IndexView(TemplateView):
#     template_name = 'home/home.html'

# queryset = Que es lo que vamos a listar
    

class ModeloPruebaListView(ListView):
    model = Prueba
    template_name = "home/home.html"
    context_object_name = "listaPrueba"
