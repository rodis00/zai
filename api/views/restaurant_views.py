from rest_framework import generics

from api.models import Restaurant
from api.serializers import restaurant_serializers as serializers


class RestaurantListView(generics.ListAPIView):
    queryset = Restaurant.objects.all()
    serializer_class = serializers.RestaurantListSerializer


class RestaurantDetailView(generics.RetrieveAPIView):
    queryset = Restaurant.objects.all()
    serializer_class = serializers.RestaurantDetailSerializer


class RestaurantCreateView(generics.CreateAPIView):
    queryset = Restaurant.objects.all()
    serializer_class = serializers.RestaurantCreateSerializer


class RestaurantUpdateView(generics.UpdateAPIView):
    queryset = Restaurant.objects.all()
    serializer_class = serializers.RestaurantUpdateSerializer


class RestaurantDeleteView(generics.DestroyAPIView):
    queryset = Restaurant.objects.all()
