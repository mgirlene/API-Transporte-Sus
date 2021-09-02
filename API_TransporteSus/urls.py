from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from accounts.views import UsuarioViewSet
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView


router = routers.DefaultRouter()
router.register(r'user',UsuarioViewSet, basename="Users")

urlpatterns = [
    path('admin/', admin.site.urls),
    path('token/', TokenObtainPairView.as_view()),
    path('token/refresh/', TokenRefreshView.as_view()),
    path('', include(router.urls))
]
