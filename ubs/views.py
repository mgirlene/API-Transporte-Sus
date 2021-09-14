from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from rest_framework.generics import ListAPIView, RetrieveAPIView
from ubs import models
from ubs import serializers

class EstadoViewSet(viewsets.ModelViewSet):
    permission_classes = (IsAuthenticated, )
    queryset = models.Estado.objects.all()
    serializer_class = serializers.EstadoSerializer

class EstadoListApiView(ListAPIView):
    queryset = models.Estado.objects.all()
    serializer_class = serializers.EstadoSerializer

class EstadoDetailApiView(RetrieveAPIView):
    queryset = models.Estado.objects.all()
    serializer_class = serializers.EstadoSerializer

class CidadeViewSet(viewsets.ModelViewSet):
    permission_classes = (IsAuthenticated, )
    queryset = models.Cidade.objects.all()
    serializer_class = serializers.CidadeSerializer

class CidadeListApiView(ListAPIView):
    queryset = models.Cidade.objects.all()
    serializer_class = serializers.CidadeSerializer

class CidadeDetailApiView(RetrieveAPIView):
    queryset = models.Cidade.objects.all()
    serializer_class = serializers.CidadeSerializer

class UbsViewSet(viewsets.ModelViewSet):
    permission_classes = (IsAuthenticated, )
    queryset = models.Ubs.objects.all()
    serializer_class = serializers.UbsSerializer

class UbsListApiView(ListAPIView):
    queryset = models.Ubs.objects.all()
    serializer_class = serializers.UbsSerializer

class UbsDetailApiView(RetrieveAPIView):
    queryset = models.Ubs.objects.all()
    serializer_class = serializers.UbsSerializer

class MotoristaViewSet(viewsets.ModelViewSet):
    permission_classes = (IsAuthenticated, )
    queryset = models.Motorista.objects.all()
    serializer_class = serializers.MotoristaSerializer

class MotoristaDetailApiView(RetrieveAPIView):
    permission_classes = (IsAuthenticated, )
    queryset = models.Motorista.objects.all()
    serializer_class = serializers.MotoristaSerializer

class MotoristaDetailUsuarioApiView(ListAPIView):
    permission_classes = (IsAuthenticated, )
    serializer_class = serializers.MotoristaSerializer

    def get_queryset(self):
        return models.Motorista.objects.filter(usuario=self.request.user.id)

class MotoristaDetailsUbsApiView(ListAPIView):
    permission_classes = (IsAuthenticated, )
    serializer_class = serializers.MotoristaSerializer

    def get_queryset(self):
        return models.Motorista.objects.filter(ubs=self.kwargs['pk'])