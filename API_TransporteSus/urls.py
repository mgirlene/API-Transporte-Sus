from django import urls
from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

from accounts.views import UsuarioCreateAPIView, UsuarioListAPIView
from ubs.views import EstadoViewSet, CidadeViewSet, UbsViewSet, MotoristaViewSet
from ubs.views import CidadeListApiView, UbsListApiView, EstadoListApiView 
from ubs.views import EstadoDetailApiView, CidadeDetailApiView, UbsDetailApiView
from ubs.views import MotoristaDetailApiView, MotoristaDetailUsuarioApiView, MotoristaDetailsUbsApiView
from agendamento.views import AgendamentoViewSet, StatusAgendamentoViewSet, AgendamentoUsuarioApiView, StatusPorAgendamentoApiView,AgendamentoDetailsUbsApiView


router = routers.DefaultRouter()

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
    path('', include(router.urls)),

    path('usuario/', UsuarioCreateAPIView.as_view()),
    path('usuariodados/', UsuarioListAPIView.as_view()),

    path('estadolist/', EstadoListApiView.as_view()),
    path('estadodetail/<int:pk>/', EstadoDetailApiView.as_view()),
    path('cidadelist/', CidadeListApiView.as_view()),
    path('cidadedetail/<int:pk>/', CidadeDetailApiView.as_view()),
    path('ubslist/', UbsListApiView.as_view()),
    path('ubsdetail/<int:pk>/', UbsDetailApiView.as_view()),

    path('motoristadetail/<int:pk>/', MotoristaDetailApiView.as_view()),
    path('motoristauser/', MotoristaDetailUsuarioApiView.as_view()),
    path('motoristaubs/<int:pk>/', MotoristaDetailsUbsApiView.as_view()),

    path('agendamentouser/', AgendamentoUsuarioApiView.as_view()),
    path('status/<int:pk>/', StatusPorAgendamentoApiView.as_view()),
    path('agendamentoubs/<int:pk>/', AgendamentoDetailsUbsApiView.as_view())
]
