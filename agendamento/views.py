from django.shortcuts import render
import agendamento
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from rest_framework.generics import ListAPIView, RetrieveAPIView

from agendamento import models
from agendamento import serializers

class AgendamentoViewSet(viewsets.ModelViewSet):
    permission_classes = (IsAuthenticated, )
    queryset = models.Agendamento.objects.all()
    serializer_class = serializers.AgendamentoSerializer
 
class AgendamentoUsuarioApiView(ListAPIView):
    permission_classes = (IsAuthenticated, )
    serializer_class = serializers.AgendamentoSerializer

    def get_queryset(self):
        return models.Agendamento.objects.filter(usuario=self.request.user.id)

class StatusAgendamentoViewSet(viewsets.ModelViewSet):
    permission_classes = (IsAuthenticated, )
    queryset = models.StatusAgendamento.objects.all()
    serializer_class = serializers.StatusAgendamentoSerializer

class StatusPorAgendamentoApiView(ListAPIView):
    permission_classes = (IsAuthenticated, )
    serializer_class = serializers.StatusAgendamentoSerializer

    def get_queryset(self, agend):
        print(self.get_object(agend))
        return models.StatusAgendamento.objects.filter(agendamento=1) # teste