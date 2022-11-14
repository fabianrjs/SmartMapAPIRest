import datetime
from django.http import Http404, HttpResponseBadRequest
from django.shortcuts import render
from django.forms import ValidationError
from django.core.exceptions import ObjectDoesNotExist
from django.http.response import JsonResponse
from rest_framework.parsers import JSONParser 
from apiRest.mockSpaceAnalytics import calcularAforo
from apiRest.models import Edificio, Nodo, Usuario, HistorialUbicacion
from apiRest.serializers import EdificioSerializer, NodoSerializer, UsuarioSerializer,HistorialUbicacionSerializer
from rest_framework.decorators import api_view
from rest_framework import status
from busquedaDeRutas import rutaMejorada

@api_view(['GET'])
def edificios(request,uId):
    if request.method == 'GET':
        try:
            usuario = Usuario.objects.get(uId = uId)
            edificio_serializer = EdificioSerializer(Edificio.objects, many = True)
            return JsonResponse(edificio_serializer.data, safe = False)
        except Usuario.DoesNotExist:
            edificios = Edificio.objects.values('id_edificio','nombre','palabras_clave',
                'descripcion','imagen','aforoActual','listaDeEntradas')
            edificio_serializer = EdificioSerializer(edificios, many = True)
            return JsonResponse(edificio_serializer.data, safe = False)
            

@api_view(['POST'])
def post_edificio(request):
    if request.method == 'POST':
        edificio_data = JSONParser().parse(request)
        edificio_serializer = EdificioSerializer(data = edificio_data)
        
        if edificio_serializer.is_valid():
            print(edificio_serializer.validated_data)
            edificio_serializer.save()
            return JsonResponse("success", safe = False)
        return JsonResponse(edificio_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET'])
def edificio(request,nombre,uId):
    if request.method == 'GET':
        try:
            usuario = Usuario.objects.get(uId = uId)
            edificio = Edificio.objects.get(nombre = nombre)
            edificio_serializer = EdificioSerializer(edificio)
            return JsonResponse(edificio_serializer.data, safe = False)
        except Usuario.DoesNotExist:
            try:
                edificio = Edificio.objects.filter(nombre = nombre).values('id_edificio','nombre','palabras_clave',
                    'descripcion','imagen','aforoActual','listaDeEntradas')
                edificio_serializer = EdificioSerializer(edificio, many = True)
                if (len(edificio_serializer.data) == 0):
                    raise Http404
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
        raise ValidationError(nodo_serializer.errors,status=status.HTTP_400_BAD_REQUEST)

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

            if(usuario.historialDeUbicaciones == None):
                usuario.historialDeUbicaciones = [] 
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
        except Usuario.DoesNotExist:
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
