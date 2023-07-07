from django.contrib import admin
from django.urls import path, include, re_path
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('admin/', admin.site.urls),
    path('cart/', include('cart.urls', namespace='cart')),
    path('', include('onlinestore.urls', namespace='onlinestore')),
    path('api/', include('api.urls')),
    path('api/auth_s/', include('rest_framework.urls')),
    path('auth/', include('register.urls')),
    path('orders/', include('orders.urls', namespace='orders')),
    path('mail/', include('mail.urls', namespace='mail')),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
