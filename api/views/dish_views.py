from rest_framework import generics

from api.models import Dish
from api.serializers import dish_serializers as serializers


class DishListView(generics.ListAPIView):
    queryset = Dish.objects.all()
    serializer_class = serializers.DishListSerializer


class DishDetailView(generics.RetrieveAPIView):
    queryset = Dish.objects.all()
    serializer_class = serializers.DishDetailSerializer


class DishCreateView(generics.CreateAPIView):
    queryset = Dish.objects.all()
    serializer_class = serializers.DishCreateSerializer


class DishUpdateView(generics.UpdateAPIView):
    queryset = Dish.objects.all()
    serializer_class = serializers.DishUpdateSerializer


class DishDeleteView(generics.DestroyAPIView):
    queryset = Dish.objects.all()
