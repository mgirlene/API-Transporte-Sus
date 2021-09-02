from django.shortcuts import render
from rest_framework import viewsets
from accounts.models import CustomUsuario
from accounts.serializer import UsuarioSerializer


class UsuarioViewSet(viewsets.ModelViewSet):
    queryset = CustomUsuario.objects.all()
    serializer_class = UsuarioSerializer
