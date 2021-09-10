from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from .models import Agendamento, StatusAgendamento
from agendamento.serializers import AgendamentoSerializer, StatusAgendamentoSerializer

class AgendamentoViewSet(viewsets.ModelViewSet):
    permission_classes = (IsAuthenticated, )
    queryset = Agendamento.objects.all()
    serializer_class = AgendamentoSerializer

class StatusAgendamentoViewSet(viewsets.ModelViewSet):
    permission_classes = (IsAuthenticated, )
    queryset = StatusAgendamento.objects.all()
    serializer_class = StatusAgendamentoSerializer