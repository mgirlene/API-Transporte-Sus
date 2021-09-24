from rest_framework import serializers
from .models import Agendamento, StatusAgendamento
from ubs.serializers import UbsSerializer
from accounts.serializers import UsuarioListSerializer

class StatusAgendamentoSerializer(serializers.ModelSerializer):
    class Meta:
        model = StatusAgendamento
        fields = '__all__'

class AgendamentoSerializer(serializers.ModelSerializer):

    def create(self, validated_data):
        status = StatusAgendamento.objects.create(status="Aguardando", observacao="...")
        print(status)

        validated_data['status'] = status

        return super(AgendamentoSerializer, self).create(validated_data)

    class Meta:
        model = Agendamento
        fields = '__all__'

class AgendamentoListSerializer(serializers.ModelSerializer):
    ubs = UbsSerializer()
    status = StatusAgendamentoSerializer()
    usuario = UsuarioListSerializer()

    class Meta:
        model = Agendamento
        fields = '__all__'