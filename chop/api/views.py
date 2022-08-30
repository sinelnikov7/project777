from django.shortcuts import render
from rest_framework import mixins, generics
from rest_framework.views import APIView
from catalog.models import *
from rest_framework.response import Response

from .paginators import NewProductPagination
from .serializers import ArticleSerializer, ProductSerializer


class ArticleAll(APIView):
    def get(self, request):
        get_data = Article.objects.all()
        ready_data = ArticleSerializer(get_data, many=True).data

        return Response(ready_data)

# class NewProduct(APIView):
#     pagination_class = NewProductPagination
#
#     def get(self, request):
#         get_data = Product.objects.all().order_by('id')
#         ready_data = ProductSerializer(get_data, many=True).data
#
#
#         return Response(ready_data)

class NewProduct(generics.ListAPIView):
    queryset = Product.objects.all().order_by('id')
    serializer_class = ProductSerializer
    pagination_class = NewProductPagination


# Create your views here.
