from rest_framework import serializers 
from .models import Usuario, logeados

class usuarioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Usuario
        fields =[
            'id_nivel',
            'apellido',
            'nombre',
        ]

class logeadosSerializer(serializers.ModelSerializer):
    class Meta:
        model = logeados
        fields =[
            'usuario',
            'ingres',
            'id_nivel',
        ]