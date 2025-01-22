# Django Rest Framework Example: Products and Categories

This project demonstrates how to use Django Rest Framework to create an API for managing `Product` and `Category`
models, and how to calculate computed fields like `total_price` and `product_total_price`.

## Views (API Endpoints)

### 1. ProductViewSet

This view handles operations related to the `Product` model. It includes a computed field `total_price`, which
calculates the total price for each product (`unit_price * quantity`).

**Code**:

```python
# views.py
class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all().select_related('category').prefetch_related('tags__category', 'tags').annotate(
        total_price=F('unit_price') * F('quantity')
    )
    serializer_class = ProductSerializer
    permission_classes = [AllowAny]
```

### 2. CategoryViewSet

This view handles operations related to the Category model. It includes a computed field product_total_price, which
calculates the total price of all related products in the category (sum(unit_price * quantity)).

**Code**:

```python
class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all().annotate(
        product_total_price=Sum(F('products__unit_price') * F('products__quantity'))
    )
    serializer_class = CategoryProductSerializer
    permission_classes = [AllowAny]
```

## Serializers

### 1. ProductSerializer

This serializer converts Product model instances into JSON. It includes a field total_price, which is computed as
unit_price * quantity for each product.

**Code**:

```python
# serializers.py
class CategoryProductSerializer(serializers.ModelSerializer):
    product_total_price = serializers.ReadOnlyField()

    class Meta:
        model = Category
        fields = '__all__'


class TagsProductSerializer(serializers.ModelSerializer):
    category = CategoryProductSerializer(many=False)

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
```

### 2. CategoryProductSerializer

This serializer converts `Category` model instances into JSON and includes the computed field `product_total_price`, which
represents the sum of unit_price * quantity for all products in the category.

**Code**:

```python
# serializers.py
class CategoryProductSerializer(serializers.ModelSerializer):
    product_total_price = serializers.ReadOnlyField()

    class Meta:
        model = Category
        fields = '__all__'
```

## Response Format

### 1. Product Response Example

The response for a `Product` includes details like the category, tags, and a computed `total_price`.

**Example**:

```json
{
  "id": 1,
  "title": "Sample Product",
  "category": {
    "id": 1,
    "title": "Sample Category"
  },
  "tags": [
    {
      "id": 1,
      "title": "Tag 1",
      "category": {
        "id": 1,
        "title": "Tag Category"
      }
    }
  ],
  "unit_price": 100.0,
  "quantity": 2,
  "total_price": 200.0
}
```

### 2. Category Response Example

The response for a Category includes a product_total_price, which is the sum of the total prices of all products in that
category.

**Example**:

```json
{
  "id": 1,
  "title": "Sample Category",
  "product_total_price": 1000.0
}
```