from django.db import models

class Edificio(models.Model):
    codigo = models.SmallIntegerField(default = 0)
    nombre = models.CharField(max_length = 70, blank = False, default = '')
    description = models.CharField(max_length = 200, blank = False, default = '')
    imagen = models.CharField(max_length = 500, default = '')
