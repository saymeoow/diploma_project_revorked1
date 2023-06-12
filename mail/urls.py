from django.urls import path
from .views import SendMailView, SuccessView

app_name = 'mail'

urlpatterns = [
    path('contact/', SendMailView.as_view(), name='contact'),
    path('success/', SuccessView.as_view(), name='success')
]
