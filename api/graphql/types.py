import graphene
from graphene_django import DjangoObjectType
from django.contrib.auth.models import User
from api.models import Address, Dish, Order, Restaurant


class DishType(DjangoObjectType):
    class Meta:
        model = Dish
        fields = "__all__"


class UserShortType(DjangoObjectType):
    class Meta:
        model = User
        fields = ["first_name", "last_name", "username", "id"]


class UserType(DjangoObjectType):
    class Meta:
        model = User
        exclude = ["password"]


class RestaurantType(DjangoObjectType):
    owner = graphene.Field(UserShortType)

    class Meta:
        model = Restaurant
        fields = "__all__"


class AddressType(DjangoObjectType):
    class Meta:
        model = Address
        fields = "__all__"


class OrderType(DjangoObjectType):
    customer = graphene.Field(UserShortType)
    total_price = graphene.Float()

    class Meta:
        model = Order
        fields = "__all__"

    def resolve_total_price(self, info):
        return self.total_price if hasattr(self, 'total_price') else None


class UserOrderStatsType(graphene.ObjectType):
    total_orders = graphene.Int()
    total_spent = graphene.Float()
    average_dish_price = graphene.Float()
