from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from ubs.models import Estado, Cidade, Ubs, Motorista
from ubs.serializers import EstadoSerializer, CidadeSerializer, UbsSerializer, MotoristaSerializer


class EstadoViewSet(viewsets.ModelViewSet):
    permission_classes = (IsAuthenticated, )
    queryset = Estado.objects.all()
    serializer_class = EstadoSerializer

class CidadeViewSet(viewsets.ModelViewSet):
    permission_classes = (IsAuthenticated, )
    queryset = Cidade.objects.all()
    serializer_class = CidadeSerializer

class UbsViewSet(viewsets.ModelViewSet):
    permission_classes = (IsAuthenticated, )
    queryset = Ubs.objects.all()
    serializer_class = UbsSerializer

class MotoristaViewSet(viewsets.ModelViewSet):
    permission_classes = (IsAuthenticated, )
    queryset = Motorista.objects.all()
    serializer_class = MotoristaSerializer