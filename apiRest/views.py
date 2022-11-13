import datetime
from django.http import Http404, HttpResponseBadRequest
from django.shortcuts import render
from django.forms import ValidationError

from django.http.response import JsonResponse
from rest_framework.parsers import JSONParser 
from rest_framework import status
from apiRest.mockSpaceAnalytics import calcularAforo
from apiRest.models import Edificio, Nodo, Usuario, HistorialUbicacion
from apiRest.serializers import EdificioSerializer, NodoSerializer, UsuarioSerializer,HistorialUbicacionSerializer
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

@api_view(['GET', 'POST'])
def usuarios(request):
    if request.method == 'GET':
        usuario_serializer = UsuarioSerializer(Usuario.objects, many = True)
        return JsonResponse(usuario_serializer.data, safe = False)
    elif request.method == 'POST':
        usuario_data = JSONParser().parse(request)
        usuario_serializer = UsuarioSerializer(data = usuario_data)
        
        if usuario_serializer.is_valid():
            print(usuario_serializer.validated_data)
            usuario_serializer.save()
            return JsonResponse("success", safe = False)
        raise ValidationError(usuario_serializer.errors)



@api_view(['GET'])
def usuario(request,uId):
    if request.method == 'GET':
        try:
            usuario = Usuario.objects.get(uId = uId)
            usuario_serializer = UsuarioSerializer(usuario)
            return JsonResponse(usuario_serializer.data, safe = False)
        except:
            raise Http404

@api_view(['PUT'])
def actualizarUbicacion(request,uId,nodoAnterior,nodoActual):
    if request.method == 'PUT':
        
        try:
            usuario = Usuario.objects.get(uId = uId)
           
            #cambiar nodo actual
            usuario.nodoActual = nodoActual

            #Añadir el nodo actual al historial
            now = datetime.datetime.now()
            nuevoNodo = HistorialUbicacion.create(nodoActual,now)

            nNodo = HistorialUbicacionSerializer(nuevoNodo) 
            usuario.historialDeUbicaciones.append(vars(nuevoNodo))
            
            #actualizar pesos de los nodos
            if(int(nodoAnterior) != -1):
                
                nodoAnt = Nodo.objects.get(idNodo = nodoAnterior)
                nodoAnt.peso = nodoAnt.peso - 1
                nodoAnt.save()

            nodoAct = Nodo.objects.get(idNodo = nodoActual)
            nodoAct.peso = nodoAct.peso + 1

            usuario.save()
            
            nodoAct.save()
           
            return JsonResponse("success", safe = False)
        except:
            raise Http404

@api_view(['PUT'])
def guardarBusqueda(request,uId,busqueda):
    if request.method == 'PUT':
        try:
            usuario = Usuario.objects.get(uId = uId)
            print("Antes: ", usuario.historialDeBusqueda)
            if(usuario.historialDeBusqueda == None):
                usuario.historialDeBusqueda = busqueda
            else:
                usuario.historialDeBusqueda += "," + busqueda

            print("Despues: ", usuario.historialDeBusqueda)
            usuario.save()
            return JsonResponse("success", safe = False)
        except:
            raise Http404

@api_view(['GET'])
def aforo(request,id_edificio):
    numPisos = 6
    if request.method == 'GET':
        if(id_edificio.isdigit()):
            aforoEdificio = calcularAforo(id_edificio,numPisos)
            return JsonResponse(aforoEdificio, safe = False)
        else:
            return HttpResponseBadRequest