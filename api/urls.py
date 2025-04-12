from django.urls import path

from . import views

urlpatterns = [
    path('auth/register/', views.UserRegisterView.as_view(), name='user-register'),

    path('users/', views.UserListView.as_view(), name='user-list'),
    path('users/<int:pk>/', views.UserDetailView.as_view(), name='user-detail'),

    path('users/<int:pk>/update/', views.UserUpdateView.as_view(), name='user-update'),
]
