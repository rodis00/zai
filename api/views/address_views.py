from rest_framework import generics, permissions

from api.models import Address
from api.serializers import address_serializers as serializers


class AddressListView(generics.ListAPIView):
    queryset = Address.objects.all()
    serializer_class = serializers.AddressListSerializer


class AddressDetailView(generics.RetrieveAPIView):
    queryset = Address.objects.all()
    serializer_class = serializers.AddressDetailSerializer


class AddressCreateView(generics.CreateAPIView):
    permission_classes = [permissions.IsAdminUser]
    queryset = Address.objects.all()
    serializer_class = serializers.AddressCreateSerializer


class AddressUpdateView(generics.UpdateAPIView):
    permission_classes = [permissions.IsAdminUser]
    queryset = Address.objects.all()
    serializer_class = serializers.AddressUpdateSerializer


class AddressDeleteView(generics.DestroyAPIView):
    permission_classes = [permissions.IsAdminUser]
    queryset = Address.objects.all()
