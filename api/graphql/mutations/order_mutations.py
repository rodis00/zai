import graphene

from api.graphql.types import OrderType
from api.models import Dish, Order
from graphql_jwt.decorators import login_required
from django.contrib.auth.models import User


class CreateOrder(graphene.Mutation):
    class Arguments:
        customer_id = graphene.Int(required=True)
        dishes = graphene.List(graphene.Int, required=True)
        payment = graphene.String(required=True)

    order = graphene.Field(OrderType)

    @login_required
    def mutate(self, info, customer_id, dishes, payment):
        try:
            customer = User.objects.get(pk=customer_id)
        except User.DoesNotExist:
            raise Exception("Customer not found")

        order = Order.objects.create(
            customer=customer,
            payment=payment
        )

        dishesList = Dish.objects.filter(id__in=dishes)
        order.dishes.set(dishesList)

        return CreateOrder(order=order)


class UpdateOrder(graphene.Mutation):
    class Arguments:
        id = graphene.Int(required=True)
        dishes = graphene.List(graphene.Int, required=False)
        payment = graphene.String(required=False)

    order = graphene.Field(OrderType)

    @login_required
    def mutate(self, info, id, dishes=None, payment=None):
        try:
            order = Order.objects.get(pk=id)
        except Order.DoesNotExist:
            raise Exception("Order not found")

        if dishes:
            dishesList = Dish.objects.filter(id__in=dishes)
            order.dishes.set(dishesList)
        if payment:
            order.payment = payment

        order.save()

        return UpdateOrder(order=order)


class DeleteOrder(graphene.Mutation):
    class Arguments:
        id = graphene.Int(required=True)

    message = graphene.Field(graphene.String)

    @login_required
    def mutate(self, info, id):
        try:
            order = Order.objects.get(pk=id)
            order.delete()
        except Order.DoesNotExist:
            raise Exception("Order not found")

        message = f"Order with id: {id} deleted"

        return DeleteOrder(message=message)


class OrderMutation(graphene.ObjectType):
    create_order = CreateOrder.Field()
    update_order = UpdateOrder.Field()
    delete_order = DeleteOrder.Field()
