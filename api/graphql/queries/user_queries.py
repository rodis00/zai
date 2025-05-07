import graphene
from graphql_jwt.decorators import login_required
from django.contrib.auth.models import User

from api.graphql.types import UserType


class UserQuery(graphene.ObjectType):
    users = graphene.List(UserType)
    user_by_id = graphene.Field(UserType, id=graphene.Int())

    @login_required
    def resolve_users(self, info):
        return User.objects.all()

    @login_required
    def resolve_user_by_id(self, info, id):
        try:
            return User.objects.get(pk=id)
        except User.DoesNotExist:
            raise Exception("User not found")
