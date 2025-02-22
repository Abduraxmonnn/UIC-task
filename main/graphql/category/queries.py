import graphene

from main.graphql.category.types import CategoryType
from main.models import Category


class CategoryAllQuery(graphene.ObjectType):
    all_categories = graphene.List(CategoryType)

    def resolve_all_categories(self, info):
        return Category.objects.all()
