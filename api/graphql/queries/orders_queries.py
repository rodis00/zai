import graphene
from graphql_jwt.decorators import login_required
from api.graphql.types import OrderType
from api.models import Order


class OrderQuery(graphene.ObjectType):
    orders = graphene.List(OrderType)
    order_by_id = graphene.Field(OrderType, id=graphene.Int())

    @login_required
    def resolve_orders(self, info):
        return Order.objects.all()

    @login_required
    def resolve_order_by_id(self, info, id):
        try:
            return Order.objects.get(pk=id)
        except Order.DoesNotExist:
            raise Exception("Order not found")
