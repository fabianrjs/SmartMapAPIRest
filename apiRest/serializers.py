from rest_framework import serializers 
from apiRest.models import Edificio

class EdificioSerializer(serializers.ModelSerializer):
 
    class Meta:
        model = Edificio
        fields = [
            'id_edificio',
            'nombre',
            'apodo',
            'descripcion',
            'imagen'
        ]