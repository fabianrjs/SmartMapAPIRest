from random import choices
from django.db import models
from django.forms import CharField
from djongo import models
from django import forms

# class Tipo_acceso(models.Model):
#     class ACCESO(models.TextChoices):
#         ESTUDIANTES = 'ES','Estudiantes'
#         DOCENTES = 'DO','Docentes'
#         ADMINS = 'AD', 'Administrativos'
#         VISITANTES = 'VI','Visitantes'

#     tipo = models.CharField(choices = ACCESO.choices)
#     class Meta:
#         abstract = True

class Espacio(models.Model):

    class TIPO_ESPACIO(models.TextChoices):
        CAFETERIA = 'CF','Cafeteria'
        AUDITORIO = 'AU','Auditorio'
        OFICINA_AD = 'OA', 'Oficina administrativa'
        OFICINA_DE = 'OD','Oficina docente'
        RESTAURANTE = 'RE','Restaurante'
        LABORATORIO = 'LAB','Laboratorio'
        SALA_ESTUDIO = 'SE','Sala de estudio'
        SALON = 'SA','Salon'
        SALA_COMPUTO = 'SC','Sala de computo' 

    nombre = models.CharField(max_length=100, default='')
    tipoEspacio = models.CharField(max_length=3, choices=TIPO_ESPACIO.choices)
    acceso = models.CharField(max_length=3,default='ES')

    class Meta:
        abstract = True
        indexes = [
            models.Index(fields=['tipoEspacio']),
            models.Index(fields=['acceso'])
        ]


class Piso(models.Model):
    nombre = models.CharField(max_length=100, default='')
    banios = models.BooleanField()
    ascensor = models.BooleanField()
    espacios = models.ArrayField(model_container=Espacio)

    class Meta:
        abstract = True


class Edificio(models.Model):
    idEdificio = models.SmallIntegerField(primary_key=True, default=0)
    nombre = models.CharField(max_length=100, default='')
    apodos = models.CharField(max_length=100, default='')
    descripcion = models.CharField(max_length=100, default='')
    pisos = models.ArrayField(model_container=Piso, default='')



class Usuario(models.Model):
    uId = models.CharField(max_length=20, primary_key=True, default='')
    email = models.CharField(max_length=50)
    nombre = models.CharField(max_length=100, default='')

class Nodo(models.Model):

    class TIPO_ESPACIO(models.TextChoices):
        GRANDE = 'grande','grande'
        MEDIANO = 'medio','mediano'
        PEQUENIO = 'pequenio', 'pequeño'

    idNodo = models.CharField(max_length=20, primary_key=True, default='')
    edEntrada = models.SmallIntegerField()
    cantidadPersonas = models.SmallIntegerField()
    tipoEspacio = models.CharField(max_length=10, choices=TIPO_ESPACIO.choices)




