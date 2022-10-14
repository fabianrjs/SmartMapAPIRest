from django.shortcuts import render

from django.http.response import JsonResponse
from rest_framework.parsers import JSONParser 
from rest_framework import status
 
from apiRest.models import Edificio
from apiRest.serializers import EdificioSerializer
from rest_framework.decorators import api_view

@api_view(['GET'])
def edificios(request):
    if request.method == 'GET': 
        edificio_serializer = EdificioSerializer(Edificio.objects, many = True)
        return JsonResponse(edificio_serializer.data, safe = False)
