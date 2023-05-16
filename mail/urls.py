from django.urls import path
from . import views

app_name = 'mail'

urlpatterns = [
    path('contact/', views.contact_view, name='contact'),
    path('success/', views.success_view, name='success'),
]
