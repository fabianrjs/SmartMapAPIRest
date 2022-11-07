from django.http import Http404
from django.shortcuts import render
from django.forms import ValidationError

from django.http.response import JsonResponse
from rest_framework.parsers import JSONParser 
from rest_framework import status
from apiRest.models import Edificio, Nodo
from apiRest.serializers import EdificioSerializer, NodoSerializer
from rest_framework.decorators import api_view

@api_view(['GET', 'POST'])
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
            return JsonResponse("success", safe = False)
        raise ValidationError(edificio_serializer.errors)

@api_view(['GET'])
def edificio(request,nombre):
    if request.method == 'GET':
        try:
            edificio = Edificio.objects.get(nombre = nombre)
            edificio_serializer = EdificioSerializer(edificio)
            return JsonResponse(edificio_serializer.data, safe = False)
        except:
            raise Http404
        
        
@api_view(['GET', 'POST'])
def nodos(request):
    if request.method == 'GET':
        nodo_serializer = NodoSerializer(Nodo.objects, many = True)
        return JsonResponse(nodo_serializer.data, safe = False)
    elif request.method == 'POST':
        nodo_data = JSONParser().parse(request)
        nodo_serializer = NodoSerializer(data = nodo_data)
        
        if nodo_serializer.is_valid():
            print(nodo_serializer.validated_data)
            nodo_serializer.save()
            return JsonResponse("success", safe = False)
        raise ValidationError(nodo_serializer.errors)

@api_view(['GET'])
def nodo(request,idNodo):
    if request.method == 'GET':
        try:
            nodo = Nodo.objects.get(idNodo = idNodo)
            nodo_serializer = NodoSerializer(nodo)
            return JsonResponse(nodo_serializer.data, safe = False)
        except:
            raise Http404
