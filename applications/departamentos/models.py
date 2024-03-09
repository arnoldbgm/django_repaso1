from django.db import models


class DepartamentosModel(models.Model):
    # Nombre => sera como figura en el administrador de Django
    name = models.CharField("Nombre", max_length=50)
    short_name = models.CharField("Nombre cort", max_length=20)
    anulate = models.BooleanField("Anulado", default=False)

    def __str__(self) -> str:
        return self.name + '-' + self.short_name
    