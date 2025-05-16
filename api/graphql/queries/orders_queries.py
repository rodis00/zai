import graphene
from graphql_jwt.decorators import login_required
from api.graphql.types import OrderType
from api.models import Order
from django.db.models import Sum


class OrderQuery(graphene.ObjectType):
    orders = graphene.List(
        OrderType, limit=graphene.Int(), offset=graphene.Int()
    )
    order_by_id = graphene.Field(OrderType, id=graphene.Int())
    user_orders = graphene.List(OrderType, user_id=graphene.Int(required=True))

    @login_required
    def resolve_orders(self, info, limit=10, offset=0):
        return Order.objects.all()[offset:offset + limit]

    @login_required
    def resolve_order_by_id(self, info, id):
        try:
            return Order.objects.get(pk=id)
        except Order.DoesNotExist:
            raise Exception("Order not found")

    @login_required
    def resolve_user_orders(self, info, user_id):
        return Order.objects.filter(customer__id=user_id).annotate(
            total_price=Sum('dishes__price')
        )
