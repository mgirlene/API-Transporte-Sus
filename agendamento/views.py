from django.shortcuts import render
from rest_framework import viewsets
from .models import Agendamento, StatusAgendamento
from agendamento.serializers import AgendamentoSerializer, StatusAgendamentoSerializer

class AgendamentoViewSet(viewsets.ModelViewSet):
    queryset = Agendamento.objects.all()
    serializer_class = AgendamentoSerializer

class StatusAgendamentoViewSet(viewsets.ModelViewSet):
    queryset = StatusAgendamento.objects.all()
    serializer_class = StatusAgendamentoSerializer