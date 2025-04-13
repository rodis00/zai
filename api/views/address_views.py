from rest_framework import generics

from api.models import Address
from api.serializers import address_serializers as serializers


class AddressListView(generics.ListAPIView):
    queryset = Address.objects.all()
    serializer_class = serializers.AddressListSerializer


class AddressDetailView(generics.RetrieveAPIView):
    queryset = Address.objects.all()
    serializer_class = serializers.AddressDetailSerializer


class AddressCreateView(generics.CreateAPIView):
    queryset = Address.objects.all()
    serializer_class = serializers.AddressCreateSerializer


class AddressUpdateView(generics.UpdateAPIView):
    queryset = Address.objects.all()
    serializer_class = serializers.AddressUpdateSerializer


class AddressDeleteView(generics.DestroyAPIView):
    queryset = Address.objects.all()
