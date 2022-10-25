from pyexpat import model
from rest_framework import serializers 
from apiRest.models import Edificio, Espacio, Nodo, Piso, Usuario


class StringArrayField(serializers.ListField):   
    child = serializers.CharField()

class EspacioSerializer(serializers.Serializer):
    nombre = serializers.CharField()
    tipoEspacio = serializers.CharField()
    acceso = StringArrayField()
    class Meta:
        model = Espacio
        #fields = ('nombre','tipoEspacio','acceso')
        

class PisoSerializer(serializers.Serializer):

    nombre = serializers.CharField()
    banios = serializers.BooleanField()
    ascensor = serializers.BooleanField()
    espacios = EspacioSerializer(many = True)
    class Meta:
        model = Piso
        #fields = ('nombre','banios','ascensor','espacios')
        

class EdificioSerializer(serializers.ModelSerializer): 
    
    idEdificio = serializers.IntegerField()
    nombre = serializers.CharField()
    apodos = serializers.CharField()
    descripcion = serializers.CharField()
    pisos = PisoSerializer(many = True)
    
    class Meta:
        model = Edificio
        fields = ('idEdificio','nombre','apodos','descripcion','pisos')

class NodoSerializer(serializers.ModelSerializer): 
    class Meta:
        model = Nodo
        fields = "__all__"

class UsuarioSerializer(serializers.ModelSerializer): 
    class Meta:
        model = Usuario
        fields = "__all__"