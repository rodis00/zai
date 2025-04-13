from rest_framework import serializers

from api.models import Address


class AddressListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Address
        fields = '__all__'


class AddressDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Address
        fields = '__all__'


class AddressCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Address
        fields = '__all__'


class AddressUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Address
        fields = '__all__'
