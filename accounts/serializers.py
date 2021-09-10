from rest_framework import serializers
from accounts.models import CustomUsuario
from django.contrib.auth.hashers import make_password

class UsuarioSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUsuario
        fields = '__all__'

    
    def create(self, validated_data):
        validated_data['password'] = make_password(validated_data['password'])
        return super(UsuarioSerializer, self).create(validated_data)