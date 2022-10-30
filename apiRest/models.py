from django.db import models

class Edificio(models.Model):
    id_edificio = models.SmallIntegerField(primary_key = True, unique = True)
    nombre = models.CharField(max_length = 100)
    apodo = models.CharField(max_length = 100, null = True)
    descripcion = models.CharField(max_length = 500)
    imagen = models.CharField(max_length = 500, null = True)
