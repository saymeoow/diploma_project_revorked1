from django.shortcuts import render
from rest_framework.decorators import action
from rest_framework.pagination import PageNumberPagination
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.pagination import PageNumberPagination
from rest_framework.response import Response
from api.serializer import SneakersSerializer
from onlinestore.models import Sneakers, Company


class SneakersPagination(PageNumberPagination):
    page_size = 3
    page_size_query_description = 'page_size'
    max_page_size = 1000


class SneakersViewSet(viewsets.ModelViewSet):
    queryset = Sneakers.objects.all()
    serializer_class = SneakersSerializer
    pagination_class = SneakersPagination
    permission_classes = [IsAuthenticated]

    @action(methods=['get'], detail=True)
    def company(self, request, pk=None):
        companies = Company.objects.get(pk=pk)
        return Response({'companies': companies.name})


# class SneakersAPI(generics.ListAPIView):
#     queryset = Sneakers.objects.all()
#     serializer_class = SneakersSerializer


# class SneakersAPI(APIView):
#     def get(self, request):
#         obj = Sneakers.objects.all()
#         return Response({'sneakers': SneakersSerializer(obj, many=True).data})
#
#     def post(self, request):
#         serializer = SneakersSerializer(data=request.data)
#         serializer.is_valid(raise_exception=True)
#         serializer.save()
#         return Response({'post': serializer.data})
#
#     def put(self, request, *args, **kwargs):
#         pk = kwargs.get("pk", None)
#         if not pk:
#             return Response({"error": "Method PUT not allowed"})
#
#         try:
#             instance = Sneakers.objects.get(pk=pk)
#         except:
#             return Response({"error": "Method PUT not allowed"})
#
#         serializer = SneakersSerializer(data=request.data, instance=instance)
#         serializer.is_valid(raise_exception=True)
#         serializer.save()
#         return Response({"post": serializer.data})


# class SneakersAPIList(generics.ListCreateAPIView):
#     queryset = Sneakers.objects.all()
#     serializer_class = SneakersSerializer
#
#
# class SneakersAPIUpdate(generics.UpdateAPIView):
#     queryset = Sneakers.objects.all()
#     serializer_class = SneakersSerializer
#
#
# class SneakersAPIUpdDel(generics.RetrieveUpdateDestroyAPIView):
#     queryset = Sneakers.objects.all()
#     serializer_class = SneakersSerializer
