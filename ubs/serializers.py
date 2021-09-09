from django.db import models
from django.db.models import fields
from rest_framework import serializers
from ubs.models import Estado, Cidade, Ubs, Motorista

class EstadoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Estado
        fields = '__all__'

class CidadeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cidade
        fields = '__all__'

class UbsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ubs
        fields = '__all__'

class MotoristaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Motorista
        fields = '__all__'