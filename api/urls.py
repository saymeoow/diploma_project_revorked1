from django.urls import path, include, re_path
from . import views
from .views import *
from rest_framework import routers

router = routers.SimpleRouter()
router.register(r'sneakers', SneakersViewSet)


app_name = 'api'

urlpatterns = [
    path('', include(router.urls)),
    path('auth_s/', include('rest_framework.urls')),
    path('auth_t/', include('djoser.urls')),
    re_path(r'^auth_t/', include('djoser.urls.authtoken')),
    ]
