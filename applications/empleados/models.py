from django.db import models
from ..departamentos.models import DepartamentosModel


class EmpleadosModel(models.Model):

    JOB_CHOICES = (
        ('0', 'CONTADOR'),
        ('1', 'ADMINISTRADOR'),
        ('2', 'ECONOMISTA'),
        ('3', 'OTROS'))

    first_name = models.CharField(
        'Primer Nombre', max_length=150)
    last_name = models.CharField('Apellido', max_length=50)
    job = models.CharField('Trabajo', max_length=50, choices=JOB_CHOICES)

    departamento = models.ForeignKey(
        DepartamentosModel, on_delete=models.CASCADE)

    # image = models.ImageField('Imagenes', upload_to=None, height_field=None, width_field=None, max_length=None)

    def __str__(self) -> str:
        return self.first_name + '-' + self.last_name
