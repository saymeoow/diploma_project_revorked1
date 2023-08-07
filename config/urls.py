from django.contrib import admin
from django.template.defaulttags import url
from django.urls import path, include, re_path
from django.conf import settings
from django.conf.urls.static import static
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView, TokenVerifyView


urlpatterns = [
    path('admin/', admin.site.urls),
    path('cart/', include('cart.urls', namespace='cart')),
    path('', include('onlinestore.urls', namespace='onlinestore')),
    path('api/', include('api.urls')),
    path('api/auth_s/', include('rest_framework.urls')),
    path('auth/', include('register.urls')),
    path('orders/', include('orders.urls', namespace='orders')),
    path('mail/', include('mail.urls', namespace='mail')),
    path('api/jwt/create/', TokenObtainPairView.as_view(), name="jwt_create"),
    path('api/jwt/refresh/', TokenRefreshView.as_view(), name="token_refresh"),
    path('api/jwt/verify/', TokenVerifyView.as_view(), name="token_verify"),
    path('oauth/', include('social_django.urls', namespace='social'))
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
