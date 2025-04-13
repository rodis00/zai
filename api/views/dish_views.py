from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import generics, permissions

from api.filters.dish_filters import DishFilter
from api.models import Dish
from api.serializers import dish_serializers as serializers


class DishListView(generics.ListAPIView):
    queryset = Dish.objects.all()
    serializer_class = serializers.DishListSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_class = DishFilter


class DishDetailView(generics.RetrieveAPIView):
    queryset = Dish.objects.all()
    serializer_class = serializers.DishDetailSerializer


class DishCreateView(generics.CreateAPIView):
    permission_classes = [permissions.IsAdminUser]
    queryset = Dish.objects.all()
    serializer_class = serializers.DishCreateSerializer


class DishUpdateView(generics.UpdateAPIView):
    permission_classes = [permissions.IsAdminUser]
    queryset = Dish.objects.all()
    serializer_class = serializers.DishUpdateSerializer


class DishDeleteView(generics.DestroyAPIView):
    permission_classes = [permissions.IsAdminUser]
    queryset = Dish.objects.all()
