from rest_framework.generics import ListAPIView, CreateAPIView
from rest_framework.permissions import IsAuthenticated
from accounts.models import CustomUsuario
from accounts.serializers import UsuarioSerializer, UsuarioListSerializer


class UsuarioCreateAPIView(CreateAPIView):
    '''CRUD de usuario'''
    queryset = CustomUsuario.objects.all()
    serializer_class = UsuarioSerializer

class UsuarioListAPIView(ListAPIView):
    '''Detalhes do usuario logado'''
    permission_classes = (IsAuthenticated, )
    serializer_class = UsuarioListSerializer

    def get_queryset(self):
        return CustomUsuario.objects.filter(email=self.request.user.email)