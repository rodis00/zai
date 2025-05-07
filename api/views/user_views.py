from django.contrib.auth.models import User
from django.db.models import Count, Sum, Avg
from rest_framework import generics, permissions, status
from rest_framework.response import Response
from rest_framework.views import APIView

from api.models import Order
from api.serializers import user_serializers


class UserRegisterView(generics.CreateAPIView):
    permission_classes = [permissions.AllowAny]
    queryset = User.objects.all()
    serializer_class = user_serializers.UserRegisterSerializer


class UserListView(generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = user_serializers.UserListSerializer


class UserDetailView(generics.RetrieveAPIView):
    queryset = User.objects.all()
    serializer_class = user_serializers.UserDetailSerializer


class UserUpdateView(generics.UpdateAPIView):
    queryset = User.objects.all()
    serializer_class = user_serializers.UserUpdateSerializer


class UserDeleteView(generics.DestroyAPIView):
    queryset = User.objects.all()


class UserOrdersView(generics.ListAPIView):
    serializer_class = user_serializers.UserOrderSerializer

    def get_queryset(self):
        user_id = self.kwargs.get('pk')
        return Order.objects.filter(customer__id=user_id).annotate(
            total_price=Sum('dishes__price')
        )


class UserOrdersStatsView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request, pk):
        try:
            user = User.objects.get(pk=pk)
        except User.DoesNotExist:
            return Response(
                {'detail': 'User not found'},
                status=status.HTTP_404_NOT_FOUND
            )

        orders = Order.objects.filter(customer=user)

        stats = orders.aggregate(
            total_orders=Count('id'),
            total_spent=Sum('dishes__price'),
            average_dish_price=Avg('dishes__price'),
        )

        return Response(stats)
