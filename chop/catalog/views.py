from django.db.models import Count
from django.shortcuts import render
from .models import *

def index(request):
    category = AnimalCategory.objects.all()
    products = Product.objects.all()[:4]
    brands = Brand.objects.all()[:5]
    feedback = Feedback.objects.all()[:1]
    articles = Article.objects.all()[:3]
    context = {
        'category': category,
        'products': products,
        'brands': brands,
        'feedback': feedback,
        'articles': articles,
    }
    # brand = Brand.objects.all().order_by('product_set')
    #
    #
    # # print(brand.product_set.count())
    # print(brand)
    brand = Brand.objects.annotate(Count('product')).order_by('-product__count')[:2]


    return render(request, 'index.html', context)
# Create your views here.
