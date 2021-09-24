from rest_framework import serializers
from ubs.models import Cidade, Ubs
# from accounts.serializers import UsuarioListSerializer

class CidadeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cidade
        fields = '__all__'

class UbsSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Ubs
        fields = '__all__'

class UbsListSerializer(serializers.ModelSerializer):
    cidade = CidadeSerializer()
    motorista = 'accounts.serializers.UsuarioListSerializer()'

    class Meta:
        model = Ubs
        fields = '__all__'