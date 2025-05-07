import graphene
import graphql_jwt

from api.graphql.mutations.address_mutations import AddressMutation
from api.graphql.mutations.dish_mutations import DishMutation
from api.graphql.mutations.order_mutations import OrderMutation
from api.graphql.mutations.restaurant_mutations import RestaurantMutation
from api.graphql.queries.address_queries import AddressQuery
from api.graphql.queries.dish_queries import DishQuery
from api.graphql.queries.orders_queries import OrderQuery
from api.graphql.queries.restaurant_queries import RestaurantQuery
from api.graphql.queries.user_queries import UserQuery


class Query(
    DishQuery,
    UserQuery,
    RestaurantQuery,
    AddressQuery,
    OrderQuery,
    graphene.ObjectType
):
    pass


class Mutation(
    DishMutation,
    AddressMutation,
    OrderMutation,
    RestaurantMutation,
    graphene.ObjectType
):
    token_auth = graphql_jwt.ObtainJSONWebToken.Field()
    verify_token = graphql_jwt.Verify.Field()
    refresh_token = graphql_jwt.Refresh.Field()


my_schema = graphene.Schema(query=Query, mutation=Mutation)
