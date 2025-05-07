import graphene
from graphql_jwt.decorators import login_required
from api.graphql.types import DishType
from api.models import Dish


class DishQuery(graphene.ObjectType):
    dishes = graphene.List(DishType)
    dish_by_id = graphene.Field(DishType, id=graphene.Int())

    @login_required
    def resolve_dishes(self, info):
        return Dish.objects.all()

    @login_required
    def resolve_dish_by_id(self, info, id):
        try:
            return Dish.objects.get(pk=id)
        except Dish.DoesNotExist:
            raise Exception("Dish not found")
