from django.shortcuts import render
from django.forms import ValidationError

from django.http.response import JsonResponse
from rest_framework.parsers import JSONParser 
from rest_framework import status
 
from apiRest.models import Edificio
from apiRest.serializers import EdificioSerializer
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
            return JsonResponse("Edificio agregado", safe = False)
        raise ValidationError(edificio_serializer.errors)
