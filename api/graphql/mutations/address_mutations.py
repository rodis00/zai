import graphene

from api.graphql.types import AddressType
from api.models import Address, Restaurant
from graphql_jwt.decorators import login_required


class CreateAddress(graphene.Mutation):
    class Arguments:
        city = graphene.String(required=True)
        country = graphene.String(required=True)
        street = graphene.String(required=True)
        zipcode = graphene.String(required=True)
        restaurant_id = graphene.Int(required=True)

    address = graphene.Field(AddressType)

    @login_required
    def mutate(self, info, city, country, street, zipcode, restaurant_id):
        try:
            restaurant = Restaurant.objects.get(pk=restaurant_id)
        except Restaurant.DoesNotExist:
            raise Exception("Restaurant not found")

        address = Address.objects.create(
            city=city,
            country=country,
            street=street,
            zipcode=zipcode,
            restaurant=restaurant
        )

        return CreateAddress(address=address)


class UpdateAddress(graphene.Mutation):
    class Arguments:
        id = graphene.Int(required=True)
        city = graphene.String(required=False)
        country = graphene.String(required=False)
        street = graphene.String(required=False)
        zipcode = graphene.String(required=False)

    address = graphene.Field(AddressType)

    @login_required
    def mutate(self, info, id, city=None, country=None, street=None, zipcode=None):
        try:
            address = Address.objects.get(pk=id)
        except Address.DoesNotExist:
            raise Exception("Address not found")

        if city:
            address.city = city
        if country:
            address.country = country
        if street:
            address.street = street
        if zipcode:
            address.zipcode = zipcode

        address.save()

        return UpdateAddress(address=address)


class DeleteAddress(graphene.Mutation):
    class Arguments:
        id = graphene.Int(required=True)

    message = graphene.Field(graphene.String)

    @login_required
    def mutate(self, info, id):
        try:
            address = Address.objects.get(pk=id)
            address.delete()
        except Address.DoesNotExist:
            raise Exception("Address not found")

        message = f"Address with id: {id} deleted"

        return DeleteAddress(message=message)


class AddressMutation(graphene.ObjectType):
    create_address = CreateAddress.Field()
    update_address = UpdateAddress.Field()
    delete_address = DeleteAddress.Field()
