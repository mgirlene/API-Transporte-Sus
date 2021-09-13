from ubs import serializers
from django.contrib.auth.models import Permission
from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.generics import ListAPIView, CreateAPIView
from rest_framework.permissions import IsAuthenticated
from accounts.models import CustomUsuario
from accounts.serializers import UsuarioSerializer, UsuarioListSerializer


class UsuarioCreateAPIView(CreateAPIView):
    queryset = CustomUsuario.objects.all()
    serializer_class = UsuarioSerializer

class UsuarioListAPIView(ListAPIView):
    permission_classes = (IsAuthenticated, )
    serializer_class = UsuarioListSerializer

    def get_queryset(self):
        usuario = self.request.user
        print(usuario)
        return CustomUsuario.objects.filter(email=self.request.user.email)