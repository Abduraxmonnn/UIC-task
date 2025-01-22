# Rest-Framework
from django.db.models import Sum, F
from rest_framework import viewsets
from rest_framework.permissions import AllowAny

# Project
from main.models import Product, Category
from main.serializers import ProductSerializer, CategoryProductSerializer


class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all().select_related('category').prefetch_related('tags__category', 'tags').annotate(
        total_price=F('unit_price') * F('quantity'))
    serializer_class = ProductSerializer
    permission_classes = [AllowAny]
    # http_method_names = ['get']


class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all().annotate(product_total_price=Sum(F('products__unit_price') * F('products__quantity')))
    serializer_class = CategoryProductSerializer
    permission_classes = [AllowAny]
    # http_method_names = ['get']
