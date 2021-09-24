from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from rest_framework.generics import ListAPIView

from agendamento import models
from agendamento import serializers

# *** MODELS AGENDAMENTOS ***

class AgendamentoViewSet(viewsets.ModelViewSet):
    '''CRUD de agendamento'''
    permission_classes = (IsAuthenticated, )
    queryset = models.Agendamento.objects.all()
    serializer_class = serializers.AgendamentoSerializer
 
class AgendamentoUsuarioApiView(ListAPIView):
    '''Listagem dos agendamentos do usuario'''
    permission_classes = (IsAuthenticated, )
    serializer_class = serializers.AgendamentoListSerializer

    def get_queryset(self):
        return models.Agendamento.objects.filter(usuario=self.request.user.id)

class AgendamentoDetailsUbsApiView(ListAPIView):
    '''Listagem dos agendamentos pela UBS'''
    permission_classes = (IsAuthenticated, )
    serializer_class = serializers.AgendamentoListSerializer

    def get_queryset(self):
        return models.Agendamento.objects.filter(ubs=self.kwargs['pk'])


# *** MODELS STATUS AGENDAMENTO ***

class StatusAgendamentoViewSet(viewsets.ModelViewSet):
    '''CRUD de StatusAgendamento'''
    permission_classes = (IsAuthenticated, )
    queryset = models.StatusAgendamento.objects.all()
    serializer_class = serializers.StatusAgendamentoSerializer