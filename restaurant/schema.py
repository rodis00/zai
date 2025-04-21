import graphene
from django.contrib.auth.models import User
from graphene_django import DjangoObjectType

from api.models import Dish


class DishType(DjangoObjectType):
    class Meta:
        model = Dish
        fields = "__all__"


class UserType(DjangoObjectType):
    class Meta:
        model = User
        fields = "__all__"


class Query(graphene.ObjectType):
    all_dishes = graphene.List(DishType)
    dish_by_id = graphene.Field(DishType, id=graphene.Int())
    user = graphene.List(UserType)

    def resolve_all_dishes(self, info):
        return Dish.objects.all()

    def resolve_dish_by_id(self, info, id):
        return Dish.objects.get(id=id)

    def resolve_user(self, info):
        return User.objects.all()


my_schema = graphene.Schema(query=Query)
