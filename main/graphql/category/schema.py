import graphene

from main.graphql.category.queries import CategoryAllQuery
from main.graphql.category.mutations import CategoryCreateMutation, CategoryUpdateMutation, CategoryDeleteMutation


class CategoryQuery(CategoryAllQuery, graphene.ObjectType):
    pass


class CategoryMutation(graphene.ObjectType):
    create_category = CategoryCreateMutation.Field()
    update_category = CategoryUpdateMutation.Field()
    delete_category = CategoryDeleteMutation.Field()

# category_schema = graphene.Schema(query=CategoryQuery, mutation=CategoryMutation)
