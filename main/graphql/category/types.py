from graphene_django import DjangoObjectType
from main.models import Category


class CategoryType(DjangoObjectType):
    class Meta:
        model = Category
        fields = ('id', 'title')
