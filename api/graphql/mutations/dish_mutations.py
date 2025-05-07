import graphene
from graphql_jwt.decorators import login_required
from api.models import Dish, Restaurant
from api.graphql.types import DishType


class CreateDish(graphene.Mutation):
    class Arguments:
        restaurant_id = graphene.Int(required=True)
        name = graphene.String(required=True)
        price = graphene.Decimal(required=True)
        description = graphene.String()
        picture = graphene.String()

    dish = graphene.Field(DishType)

    @login_required
    def mutate(self, info, restaurant_id, name, price, description=None, picture=None):
        try:
            restaurant = Restaurant.objects.get(pk=restaurant_id)
        except Restaurant.DoesNotExist:
            raise Exception("Restaurant not found")

        dish = Dish.objects.create(
            restaurant=restaurant,
            name=name,
            price=price,
            description=description,
            picture=picture,
        )
        return CreateDish(dish=dish)


class UpdateDish(graphene.Mutation):
    class Arguments:
        id = graphene.ID(required=True)
        name = graphene.String()
        price = graphene.Decimal()
        description = graphene.String()
        picture = graphene.String()

    dish = graphene.Field(DishType)

    @login_required
    def mutate(self, info, id, name=None, price=None, description=None, picture=None):
        try:
            dish = Dish.objects.get(pk=id)
        except Dish.DoesNotExist:
            raise Exception("Dish not found")

        if name:
            dish.name = name
        if price:
            dish.price = price
        if description:
            dish.description = description
        if picture:
            dish.picture = picture

        dish.save()

        return UpdateDish(dish=dish)


class DeleteDish(graphene.Mutation):
    class Arguments:
        id = graphene.Int(required=True)

    message = graphene.Field(graphene.String)

    @login_required
    def mutate(self, info, id):
        try:
            dish = Dish.objects.get(pk=id)
            dish.delete()
        except Dish.DoesNotExist:
            raise Exception("Dish not found")

        message = f"Dish with id: {id} deleted"

        return DeleteDish(message=message)


class DishMutation(graphene.ObjectType):
    create_dish = CreateDish.Field()
    update_dish = UpdateDish.Field()
    delete_dish = DeleteDish.Field()
