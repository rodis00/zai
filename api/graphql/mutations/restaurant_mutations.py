import graphene

from api.graphql.types import RestaurantType
from api.models import Restaurant
from graphql_jwt.decorators import login_required
from django.contrib.auth.models import User


class CreateRestaurant(graphene.Mutation):
    class Arguments:
        name = graphene.String(required=True)
        owner_id = graphene.Int(required=True)

    restaurant = graphene.Field(RestaurantType)

    @login_required
    def mutate(self, info, name, owner_id):
        try:
            owner = User.objects.get(pk=owner_id)
        except User.DoesNotExist:
            raise Exception("User not found")

        restaurant = Restaurant.objects.create(
            name=name,
            owner=owner
        )

        return CreateRestaurant(restaurant=restaurant)


class UpdateRestaurant(graphene.Mutation):
    class Arguments:
        id = graphene.Int(required=True)
        name = graphene.String(required=False)

    restaurant = graphene.Field(RestaurantType)

    @login_required
    def mutate(self, info, id, name=None):
        try:
            restaurnat = Restaurant.objects.get(pk=id)
        except Restaurant.DoesNotExist:
            raise Exception("Restaurant not found")

        if name:
            restaurnat.name = name

        restaurnat.save()

        return UpdateRestaurant(restaurnat=restaurnat)


class DeleteRestaurant(graphene.Mutation):
    class Arguments:
        id = graphene.Int(required=True)

    message = graphene.Field(graphene.String)

    @login_required
    def mutate(self, info, id):
        try:
            restaurant = Restaurant.objects.get(pk=id)
            restaurant.delete()
        except Restaurant.DoesNotExist:
            raise Exception("Restaurant not found")

        message = f"Restaurant with id: {id} deleted"

        return DeleteRestaurant(message=message)


class RestaurantMutation(graphene.ObjectType):
    create_restaurant = CreateRestaurant.Field()
    update_restaurant = UpdateRestaurant.Field()
    delete_restaurant = DeleteRestaurant.Field()
