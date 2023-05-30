from django.urls import path
from . import views
from .views import ProfileShow, ProfilePersonal, Register, Login, Logout

app_name = 'auth'

urlpatterns = [
    path('login/', Login.as_view(),
         name='login'),
    path('logout/', Logout.as_view(),
         name='logouts'),
    path('register/', Register.as_view(),
         name='register'),
    path('edit_profile/', views.edit,
         name='edit'),
    path('profile/', ProfileShow.as_view(),
         name='profile'),
    path('profile_personal/', ProfilePersonal.as_view(),
         name='profile_personal')
]