import graphene
from graphql_jwt.decorators import login_required
from django.contrib.auth.models import User

from api.graphql.types import UserType


class UserQuery(graphene.ObjectType):
    users = graphene.List(
        UserType, limit=graphene.Int(), offset=graphene.Int()
    )
    user_by_id = graphene.Field(UserType, id=graphene.Int())

    @login_required
    def resolve_users(self, info, limit=10, offset=0):
        return User.objects.all()[offset:offset + limit]

    @login_required
    def resolve_user_by_id(self, info, id):
        try:
            return User.objects.get(pk=id)
        except User.DoesNotExist:
            raise Exception("User not found")
