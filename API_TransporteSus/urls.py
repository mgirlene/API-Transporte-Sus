from django import urls
from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from accounts.views import UsuarioViewSet
from ubs.views import EstadoViewSet, CidadeViewSet, UbsViewSet, MotoristaViewSet
from agendamento.views import AgendamentoViewSet, StatusAgendamentoViewSet
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView


router = routers.DefaultRouter()
router.register(r'usuario', UsuarioViewSet, basename="Usuarios")

router.register(r'estado', EstadoViewSet, basename="Estados")
router.register(r'cidade', CidadeViewSet, basename="Cidades")
router.register(r'ubs', UbsViewSet, basename="Ubs")
router.register(r'motorista', MotoristaViewSet, basename="Motoristas")

router.register(r'agendamento', AgendamentoViewSet, basename="Agendamentos")
router.register(r'statusagendamento', StatusAgendamentoViewSet, basename="StatusAgendamentos")

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api-auth/', include('rest_framework.urls')),
    path('token/', TokenObtainPairView.as_view()),
    path('token/refresh/', TokenRefreshView.as_view()),
    path('', include(router.urls))
]
