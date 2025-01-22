from rest_framework import serializers

from main.models import Product, Category, Tag, TagsCategory


class CategoryProductSerializer(serializers.ModelSerializer):
    product_total_price = serializers.ReadOnlyField()

    class Meta:
        model = Category
        fields = '__all__'


class TagCategoryProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = TagsCategory
        fields = '__all__'


class TagsProductSerializer(serializers.ModelSerializer):
    category = TagCategoryProductSerializer(many=False)

    class Meta:
        model = Tag
        fields = '__all__'


class ProductSerializer(serializers.ModelSerializer):
    category = CategoryProductSerializer(many=False)
    tags = TagsProductSerializer(many=True)
    total_price = serializers.ReadOnlyField()

    class Meta:
        model = Product
        fields = '__all__'
