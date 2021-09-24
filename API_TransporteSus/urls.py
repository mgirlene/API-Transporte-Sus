from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

from accounts.views import UsuarioCreateAPIView, UsuarioListAPIView
from ubs.views import CidadeViewSet, CidadeListApiView, CidadeDetailApiView
from ubs.views import UbsViewSet, UbsListApiView, UbsDetailApiView, UbsDetailMotoristaApiView, UbsDetailCidadeApiView
from agendamento.views import AgendamentoViewSet, AgendamentoUsuarioApiView, AgendamentoDetailsUbsApiView, StatusAgendamentoViewSet


router = routers.DefaultRouter()

router.register(r'cidade', CidadeViewSet, basename="Cidades")
router.register(r'ubs', UbsViewSet, basename="Ubs")
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

    path('cidadelist/', CidadeListApiView.as_view()),
    path('cidadedetail/<int:pk>/', CidadeDetailApiView.as_view()),

    path('ubslist/', UbsListApiView.as_view()),
    path('ubsdetail/<int:pk>/', UbsDetailApiView.as_view()),
    path('ubsdetailmotorista/', UbsDetailMotoristaApiView.as_view()),
    path('ubsdetailcidade/<int:pk>/', UbsDetailCidadeApiView.as_view()),

    path('agendamentouser/', AgendamentoUsuarioApiView.as_view()),
    path('agendamentoubs/<int:pk>/', AgendamentoDetailsUbsApiView.as_view()),
]
