from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from rest_framework.generics import ListAPIView, RetrieveAPIView
from ubs import models
from ubs import serializers

# *** MODELS CIDADE ***

class CidadeViewSet(viewsets.ModelViewSet):
    '''CRUD de Cidade'''
    permission_classes = (IsAuthenticated, )
    queryset = models.Cidade.objects.all()
    serializer_class = serializers.CidadeSerializer

class CidadeListApiView(ListAPIView):
    '''Listagem de cidade SEM AUTENTICAÇÃO'''
    queryset = models.Cidade.objects.all()
    serializer_class = serializers.CidadeSerializer

class CidadeDetailApiView(RetrieveAPIView):
    '''Detalhes de cidade SEM AUTENTICAÇÃO'''
    queryset = models.Cidade.objects.all()
    serializer_class = serializers.CidadeSerializer


# *** MODELS UBS ***

class UbsViewSet(viewsets.ModelViewSet):
    '''CRUD de Ubs'''
    permission_classes = (IsAuthenticated, )
    queryset = models.Ubs.objects.all()
    serializer_class = serializers.UbsSerializer

class UbsListApiView(ListAPIView):
    '''Listagem de UBS SEM AUTENTICAÇÃO'''
    queryset = models.Ubs.objects.all()
    serializer_class = serializers.UbsListSerializer

class UbsDetailApiView(RetrieveAPIView):
    '''Detalhes de UBS SEM AUTENTICAÇÃO'''
    queryset = models.Ubs.objects.all()
    serializer_class = serializers.UbsListSerializer

class UbsDetailMotoristaApiView(ListAPIView):
    '''Listagem de UBS pelo id do Motorista'''
    permission_classes = (IsAuthenticated, )
    serializer_class = serializers.UbsListSerializer

    def get_queryset(self):
        return models.Ubs.objects.filter(motorista=self.request.user.id)

class UbsDetailCidadeApiView(ListAPIView):
    '''Listagem de UBS pelo id da Cidade'''
    permission_classes = (IsAuthenticated, )
    serializer_class = serializers.UbsListSerializer

    def get_queryset(self):
        return models.Ubs.objects.filter(cidade=self.kwargs['pk'])