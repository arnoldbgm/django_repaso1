from django.db import models
from ..departamentos.models import DepartamentosModel
from ckeditor.fields import RichTextField

class HabilidadesModel(models.Model):
    """Cada empleado ahora tendra un conjunto de habilidades"""
    habilidades = models.CharField('Habilidad', max_length=50)


    class Meta:
        verbose_name = 'Habilidad'
        verbose_name_plural = 'Habilidades en general'

    def __str__(self) -> str:
        return self.habilidades


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
    habilidades = models.ManyToManyField(HabilidadesModel)
    content_cv = RichTextField()
    # image = models.ImageField('Imagenes', upload_to=None, height_field=None, width_field=None, max_length=None)


    class Meta:
        verbose_name = 'Empleado'
        verbose_name_plural = 'Empleados de la empresa'
