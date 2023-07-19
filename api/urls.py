from django.urls import path, include, re_path
from . import views
from .views import *
from rest_framework import routers
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView, TokenVerifyView

router = routers.SimpleRouter()
router.register(r'sneakers', SneakersViewSet)


app_name = 'api'

urlpatterns = [
    path('', include(router.urls)),
    path('auth_s/', include('rest_framework.urls')),
    path('auth_t/', include('djoser.urls')),
    re_path(r'^auth_t/', include('djoser.urls.authtoken')),
    path('jwt/create/', TokenObtainPairView.as_view(), name="jwt_create"),
    path('jwt/refresh/', TokenRefreshView.as_view(), name="token_refresh"),
    path('jwt/verify/', TokenVerifyView.as_view(), name="token_verify")
    ]
