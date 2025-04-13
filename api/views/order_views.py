from rest_framework import generics

from api.models import Order
from api.serializers import order_serializers as serializers


class OrderListView(generics.ListAPIView):
    queryset = Order.objects.all()
    serializer_class = serializers.OrderListSerializer


class OrderDetailView(generics.RetrieveAPIView):
    queryset = Order.objects.all()
    serializer_class = serializers.OrderDetailSerializer


class OrderCreateView(generics.CreateAPIView):
    queryset = Order.objects.all()
    serializer_class = serializers.OrderCreateSerializer


class OrderUpdateView(generics.UpdateAPIView):
    queryset = Order.objects.all()
    serializer_class = serializers.OrderUpdateSerializer


class OrderDeleteView(generics.DestroyAPIView):
    queryset = Order.objects.all()
