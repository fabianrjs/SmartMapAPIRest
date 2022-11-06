from rest_framework import serializers 
from apiRest.models import Edificio, Espacio, Nodo


class EspacioSerializer(serializers.Serializer):
     
    nombre = serializers.CharField(allow_null = True)
    sePuedeComer = serializers.BooleanField(allow_null = True)
    tipoEspacio = serializers.CharField(allow_null = True)
    prestamoEquipos = serializers.BooleanField(allow_null = True)
    
    class Meta:
            model = Espacio
            fields = [
                'nombre',
                'sePuedeComer',
                'tipoEspacio',
                'prestamoEquipos'
            ]

class EdificioSerializer(serializers.ModelSerializer):
 
    espacios = EspacioSerializer(many = True, allow_null = True)
    class Meta:
        model = Edificio
        fields = [
            'id_edificio',
            'nombre',
            'apodo',
            'descripcion',
            'imagen',
            'aforoActual',
            'espacios',
            'listaDeEntradas'
        ]

class NodoSerializer(serializers.ModelSerializer):

    class Meta:
        model = Nodo
        fields = [
            'idNodo',
            'peso',
            'habilitado',
            'vecinos',
            'tipoEspacio',
          
        ]