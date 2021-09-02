from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from accounts.views import UsuarioViewSet
from ubs.views import EstadoViewSet, CidadeViewSet, UbsViewSet
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView


router = routers.DefaultRouter()
router.register(r'user', UsuarioViewSet, basename="Users")
router.register(r'estado', EstadoViewSet, basename="Estados")
router.register(r'cidade', CidadeViewSet, basename="Cidades")
router.register(r'ubs', UbsViewSet, basename="Ubs")

urlpatterns = [
    path('admin/', admin.site.urls),
    path('token/', TokenObtainPairView.as_view()),
    path('token/refresh/', TokenRefreshView.as_view()),
    path('', include(router.urls))
]
