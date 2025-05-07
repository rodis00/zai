import graphene
from graphql_jwt.decorators import login_required
from api.graphql.types import AddressType
from api.models import Address


class AddressQuery(graphene.ObjectType):
    addresses = graphene.List(AddressType)
    address_by_id = graphene.Field(AddressType, id=graphene.Int())

    @login_required
    def resolve_addresses(self, info):
        return Address.objects.all()

    @login_required
    def resolve_address_by_id(self, info, id):
        try:
            return Address.objects.get(pk=id)
        except Address.DoesNotExist:
            raise Exception("Address not found")
