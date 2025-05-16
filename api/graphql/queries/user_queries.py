import graphene
from graphql_jwt.decorators import login_required
from django.contrib.auth.models import User

from api.graphql.types import UserOrderStatsType, UserType
from api.models import Order
from django.db.models import Count, Sum, Avg


class UserQuery(graphene.ObjectType):
    users = graphene.List(
        UserType, limit=graphene.Int(), offset=graphene.Int()
    )
    user_by_id = graphene.Field(UserType, id=graphene.Int())
    user_order_stats = graphene.Field(
        UserOrderStatsType, user_id=graphene.Int(required=True))

    @login_required
    def resolve_users(self, info, limit=10, offset=0):
        return User.objects.all()[offset:offset + limit]

    @login_required
    def resolve_user_by_id(self, info, id):
        try:
            return User.objects.get(pk=id)
        except User.DoesNotExist:
            raise Exception("User not found")

    @login_required
    def resolve_user_order_stats(self, info, user_id):
        try:
            user = User.objects.get(pk=user_id)
        except User.DoesNotExist:
            raise Exception("User not found")

        stats = Order.objects.filter(customer=user).aggregate(
            total_orders=Count('id'),
            total_spent=Sum('dishes__price'),
            average_dish_price=Avg('dishes__price'),
        )

        return UserOrderStatsType(
            total_orders=stats['total_orders'] or 0,
            total_spent=stats['total_spent'] or 0.0,
            average_dish_price=stats['average_dish_price'] or 0.0,
        )
