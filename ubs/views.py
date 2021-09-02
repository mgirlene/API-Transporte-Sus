from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from ubs.models import Estado, Cidade, Ubs
from ubs.serializer import EstadoSerializer, CidadeSerializer, UbsSerializer


class EstadoViewSet(viewsets.ModelViewSet):
    permission_classes = (IsAuthenticated, )
    queryset = Estado.objects.all()
    serializer_class = EstadoSerializer

class CidadeViewSet(viewsets.ModelViewSet):
    queryset = Cidade.objects.all()
    serializer_class = CidadeSerializer

class UbsViewSet(viewsets.ModelViewSet):
    queryset = Ubs.objects.all()
    serializer_class = UbsSerializer
