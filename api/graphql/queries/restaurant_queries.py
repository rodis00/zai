import graphene
from graphql_jwt.decorators import login_required

from api.graphql.types import RestaurantType
from api.models import Restaurant


class RestaurantQuery(graphene.ObjectType):
    restaurants = graphene.List(
        RestaurantType, limit=graphene.Int(), offset=graphene.Int()
    )
    restaurant_by_id = graphene.Field(RestaurantType, id=graphene.Int())

    @login_required
    def resolve_restaurants(self, info, limit=10, offset=0):
        return Restaurant.objects.all()[offset:offset + limit]

    @login_required
    def resolve_restaurant_by_id(self, info, id):
        try:
            return Restaurant.objects.get(pk=id)
        except Restaurant.DoesNotExist:
            raise Exception("Restaurant not found")
