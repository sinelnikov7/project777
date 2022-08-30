from rest_framework import serializers
from catalog.models import *




class ProductCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductCategory
        fields = '__all__'


class ArticleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Article
        # fields = '__all__'
        exclude = ('owner',)


class FeedbackSerializer(serializers.ModelSerializer):
    class Meta:
        model = Feedback
        fields = '__all__'


class ProductSerializer(serializers.ModelSerializer):
    productcategory = ProductCategorySerializer()
    class Meta:
        model = Product
        fields = '__all__'

class BrandSerializer(serializers.ModelSerializer):

    class Meta:
        model = Brand
        depth = 1
        fields = ('id','name','image', 'product_set',)


