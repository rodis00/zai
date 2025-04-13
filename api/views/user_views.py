from django.contrib.auth.models import User
from rest_framework import generics, permissions

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
