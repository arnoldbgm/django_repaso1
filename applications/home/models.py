from django.db import models


class Prueba(models.Model):
    titulo  = models.CharField( max_length=50)
    sub_titulo  = models.CharField( max_length=50)