from django.db.models import Count
from rest_framework import viewsets, mixins
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from rest_framework.viewsets import GenericViewSet
from django_filters.rest_framework import DjangoFilterBackend

from .paginators import ArticleListPagination, FeedbackListPagination
from .permissions import IsOwnerOrReadOnly
from .serializers import ArticleSerializer, FeedbackSerializer, BrandSerializer, ProductSerializer, \
    AnimalCategorySerializer, ProductCategorySerializer
from catalog.models import *


class ArticleViewSet(viewsets.ModelViewSet):
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer
    pagination_class = ArticleListPagination
    permission_classes = (IsAuthenticatedOrReadOnly,) #IsOwnerOrReadOnly)

class FeedbackViewSet(mixins.CreateModelMixin,
                       mixins.RetrieveModelMixin,
                       mixins.ListModelMixin,
                       GenericViewSet):

    queryset = Feedback.objects.all()
    serializer_class = FeedbackSerializer
    pagination_class = FeedbackListPagination

class BrandViewSet(viewsets.ModelViewSet):
    queryset = Brand.objects.annotate(Count('product')).order_by('-product__count')[:5]
    serializer_class = BrandSerializer

class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all().order_by('-id')
    serializer_class = ProductSerializer
    filter_backends = [DjangoFilterBackend, ]
    filterset_fields = ['animalcategory', 'productcategory', 'brand']

    # def get_queryset(self):
    #     p = Product.objects.all()
    #     print(self.request.query_params)
    #     return p

class AnimalCategoryViewSet(viewsets.ModelViewSet):
    queryset = AnimalCategory.objects.all()
    serializer_class = AnimalCategorySerializer


class ProductCategoryViewSet(viewsets.ModelViewSet):
    queryset = ProductCategory.objects.all()
    serializer_class = ProductCategorySerializer
