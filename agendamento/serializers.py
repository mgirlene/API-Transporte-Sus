from django.db import models
from rest_framework import serializers
from .models import Agendamento, StatusAgendamento

class AgendamentoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Agendamento
        fields = '__all__'

class StatusAgendamentoSerializer(serializers.ModelSerializer):
    class Meta:
        model = StatusAgendamento
        fields = '__all__'