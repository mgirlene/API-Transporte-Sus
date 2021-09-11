from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from ubs.models import Estado, Cidade, Ubs, Motorista
from ubs.serializers import EstadoSerializer, CidadeSerializer, UbsSerializer, MotoristaSerializer

from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.exceptions import NotFound

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



class EstadoList(APIView):
    def get(self, request):
        estado = Estado.objects.all()
        serializer = EstadoSerializer(estado, many=True)
        return Response(serializer.data)

class EstadoDetail(APIView):

    def get_object(self, pk):
        try:
            return Estado.objects.get(pk=pk)
        except Estado.DoesNotExist:
            raise NotFound()

    def get(self, request, pk):
        estado = self.get_object(pk)
        serializer = EstadoSerializer(estado)
        return Response(serializer.data)

class CidadeList(APIView):
    def get(self, request):
        cidade = Cidade.objects.all()
        serializer = CidadeSerializer(cidade, many=True)
        return Response(serializer.data)

class CidadeDetail(APIView):

    def get_object(self, pk):
        try:
            return Cidade.objects.get(pk=pk)
        except Cidade.DoesNotExist:
            raise NotFound()

    def get(self, request, pk):
        cidade = self.get_object(pk)
        serializer = CidadeSerializer(cidade)
        return Response(serializer.data)

class UbsList(APIView):
    def get(self, request):
        ubs = Ubs.objects.all()
        serializer = UbsSerializer(ubs, many=True)
        return Response(serializer.data)

class UbsDetail(APIView):

    def get_object(self, pk):
        try:
            return Ubs.objects.get(pk=pk)
        except Ubs.DoesNotExist:
            raise NotFound()

    def get(self, request, pk):
        ubs = self.get_object(pk)
        serializer = UbsSerializer(ubs)
        return Response(serializer.data)