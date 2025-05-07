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

    class Meta:
        model = Order
        fields = "__all__"
