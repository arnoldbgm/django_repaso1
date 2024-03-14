
from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('listar-empleados/', views.ListAllEmpleados.as_view()),
    path('listar-por-areas/<shortname>/', views.ListByAreaEmpleados.as_view())
]
