from rest_framework import serializers

from api.models import Restaurant


class RestaurantListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Restaurant
        fields = '__all__'


class RestaurantDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Restaurant
        fields = '__all__'


class RestaurantCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Restaurant
        fields = '__all__'


class RestaurantUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Restaurant
        fields = '__all__'
