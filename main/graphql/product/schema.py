import graphene

from main.graphql.product.queries import ProductAllQuery, ProductRetrieveQuery


class ProductQuery(ProductAllQuery, ProductRetrieveQuery, graphene.ObjectType):
    pass


# product_schema = graphene.Schema(query=ProductQuery)


"""
query retrieveDifferentProducts {
  product1: retrieveProduct(id: 1) {
    id
    title
    unitPrice
    category {
      title
    }
  }
  product2: retrieveProduct(id: 2) {
    id
    title
    unitPrice
  }
  product3: retrieveProduct(id: 3) {
    id
    title
    quantity
    unitPrice
    tags {
      title
    }
  }
}
"""
