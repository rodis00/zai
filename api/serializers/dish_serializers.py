from rest_framework import serializers

from api.models import Dish


class DishListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Dish
        fields = '__all__'


class DishDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Dish
        fields = '__all__'


class DishCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Dish
        fields = '__all__'


class DishUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Dish
        fields = '__all__'
