from django.urls import path
from . import views
from .views import SneakersList, SneakersCompany, SneakersDetail, Support, AddSneakersView, FakeUrlComment, Search

app_name = 'store'

urlpatterns = [
    path('support', Support.as_view(),
         name='support'),
    path('', SneakersList.as_view(),
         name='sneakers_list'),
    path('<slug:company_slug>/', SneakersCompany.as_view(),
         name='company'),
    path('<int:id>/<slug:slug>', SneakersDetail.as_view(),
         name='sneakers_detail'),
    path('add_sneakers', AddSneakersView.as_view(),
         name='add_sneakers'),
    path('thanks_for_comment', FakeUrlComment.as_view(),
         name='fake'),
    path('search', Search.as_view(),
         name='search')
]
