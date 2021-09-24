from rest_framework import serializers
from accounts.models import CustomUsuario
from django.contrib.auth.hashers import make_password
from ubs.serializers import CidadeSerializer

class UsuarioSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = CustomUsuario
        fields = '__all__'
    
    def create(self, validated_data):
        validated_data['password'] = make_password(validated_data['password'])
        return super(UsuarioSerializer, self).create(validated_data)

class UsuarioListSerializer(serializers.ModelSerializer):

    cidade = CidadeSerializer()

    class Meta:
        model = CustomUsuario
        fields = ['id', 'first_name', 'email', 'motorista_ubs', 'cidade', 'localizacao']