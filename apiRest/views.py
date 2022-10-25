import io
import json
import string
from django.forms import ValidationError
from django.shortcuts import render

from django.http.response import JsonResponse
from rest_framework.parsers import JSONParser 
from rest_framework import status
from rest_framework.parsers import JSONParser
from rest_framework.renderers import JSONRenderer
from apiRest.models import Edificio, Nodo, Usuario
from apiRest.serializers import EdificioSerializer, NodoSerializer, UsuarioSerializer
from rest_framework.decorators import api_view

class PisoPModel:
        def __init__(self, nombre, banios, ascensor, espacios):
            self.nombre = nombre
            self.banios = banios
            self.ascensor = ascensor
            self.espacios = espacios

        @classmethod
        def from_json(cls,jsonString):
            json_dict = jsonString
            return cls(**json_dict)

class edificioPModel:
    def __init__(self, idEdificio, nombre, apodos, descripcion, pisos):
        self.idEdificio = idEdificio
        self.nombre = nombre
        self.apodos = apodos
        self.descripcion =  descripcion
        self.pisos = pisos

    @classmethod
    def from_json(cls,jsonString):
        json_dict = jsonString
        return cls(**json_dict)

    

#----EDIFICIOS-------------------------------------------------------

@api_view(['GET','POST'])
def edificios(request):
    if request.method == 'GET': 
        edificio_serializer = EdificioSerializer(Edificio.objects, many = True)
        return JsonResponse(edificio_serializer.data, safe = False)
    elif request.method == 'POST':
        edificio_data = JSONParser().parse(request)
        edificio_serializer = EdificioSerializer(data = edificio_data)
        
        if edificio_serializer.is_valid():
            print(edificio_serializer.validated_data)
            edificio_serializer.save()
            return JsonResponse("Edificio agregado", safe = False)
        raise ValidationError(edificio_serializer.errors)

@api_view(['GET'])
def edificio(request,nombre):
    if request.method == 'GET':
        edificio = Edificio.objects.get(nombre = nombre)
        edificio_serializer = EdificioSerializer(edificio)
        return JsonResponse(edificio_serializer.data, safe = False) 

#----USUARIOS-------------------------------------------------------

@api_view(['GET','POST'])
def usuarios(request):
    if request.method == 'GET':
        usuario_serializer = UsuarioSerializer(Usuario.objects, many = True)
        return JsonResponse(usuario_serializer.data, safe = False)
    elif request.method == 'POST':
        usuario_data = JSONParser().parse(request)
        usuario_serializer = UsuarioSerializer(data = usuario_data)
        if usuario_serializer.is_valid():
            usuario_serializer.save()
            return JsonResponse("usuario agregado", safe = False)
        return JsonResponse("fallo", safe = False)

#----NODOS-------------------------------------------------------

@api_view(['GET','POST'])
def nodos(request):
    if request.method == 'GET':
        nodo_serializer = NodoSerializer(Nodo.objects, many = True)
        return JsonResponse(nodo_serializer.data, safe = False)
    elif request.method == 'POST':
        nodo_data = JSONParser().parse(request)
        nodo_serializer = NodoSerializer(data = nodo_data)
        if nodo_serializer.is_valid():
            nodo_serializer.save()
            return JsonResponse("nodo agregado", safe = False)
        return JsonResponse("fallo", safe = False)
    

@api_view(['GET'])
def nodo(request, idNodo):
    if request.method == 'GET':
        nodo = Nodo.objects.get(idNodo = idNodo)
        nodo_serializer = NodoSerializer(nodo)
        nodoModel = JsonResponse(nodo_serializer.data, safe = False).getvalue()
        print("------------------------------------------")
        #my_json = nodoModel.decode('utf8').replace("'", '"')  
        print(nodoModel)
        print("------------------------------------------")
        return JsonResponse(nodo_serializer.data, safe = False)



