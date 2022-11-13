from django.http import Http404
from django.shortcuts import render
from django.forms import ValidationError

from django.http.response import JsonResponse
from rest_framework.parsers import JSONParser 
from apiRest.models import Edificio, Nodo, Usuario
from apiRest.serializers import EdificioSerializer, NodoSerializer, UsuarioSerializer
from rest_framework.decorators import api_view

from busquedaDeRutas import rutaMejorada

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

@api_view(['GET'])
def ruta(request, idNodoInicio, idNodoFinal):
    if request.method == 'GET':
        try:
            if (str(idNodoInicio).isdigit() and str(idNodoFinal).isdigit()):
                nodosdb = NodoSerializer(Nodo.objects, many = True)
                nodos = []
                for nodo in nodosdb.data:
                    nodos.append(
                        rutaMejorada.Nodo(
                            idNodo = nodo['idNodo'],
                            peso = nodo['peso'],
                            tipoEspacio = nodo['tipoEspacio'],
                            vecinos = nodo['vecinos'],
                            habilitado = nodo['habilitado']
                        )
                    )
                ruta = rutaMejorada.buscarRutaOptima(nodos, int(idNodoInicio), int(idNodoFinal))
                return JsonResponse({'ruta': ruta}, safe = False)
            else:
                return JsonResponse("failed", safe = False)
        except Exception as e:
            print('--------')
            print(e)
            print('--------')
            raise Http404
