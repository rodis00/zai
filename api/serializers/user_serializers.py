from django.contrib.auth.models import User
from rest_framework import serializers

from api.models import Order
from api.serializers import dish_serializers


class UserRegisterSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)

    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'password']

    def create(self, validated_data):
        user = User.objects.create_user(**validated_data)
        return user


class UserListSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'email']


class UserDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'first_name', 'last_name']


class UserUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'first_name', 'last_name']

    def update(self, instance, validated_data):
        instance.username = validated_data.get('username', instance.username)
        instance.email = validated_data.get('email', instance.email)
        instance.first_name = validated_data.get(
            'first_name', instance.first_name
        )
        instance.last_name = validated_data.get(
            'last_name', instance.last_name
        )

        instance.save()

        return instance


class UserOrderSerializer(serializers.ModelSerializer):
    dishes = dish_serializers.DishInfoSerializer(many=True, read_only=True)
    total_price = serializers.DecimalField(
        max_digits=10, decimal_places=2, read_only=True
    )

    class Meta:
        model = Order
        fields = ['id', 'payment', 'created_at', 'dishes', 'total_price']
