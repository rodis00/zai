from django.urls import path

from . import views

urlpatterns = [
    # auth
    path('auth/register/', views.UserRegisterView.as_view(), name='user-register'),

    # user
    path('users/', views.UserListView.as_view(), name='user-list'),
    path('users/<int:pk>/', views.UserDetailView.as_view(), name='user-detail'),
    path('users/<int:pk>/update/', views.UserUpdateView.as_view(), name='user-update'),
    path('users/<int:pk>/delete/', views.UserDeleteView.as_view(), name='user-delete'),

    # restaurant
    path('restaurants/', views.RestaurantListView.as_view(), name='restaurant-list'),
    path('restaurants/create/', views.RestaurantCreateView.as_view(), name='restaurant-create'),
    path('restaurants/<int:pk>/', views.RestaurantDetailView.as_view(), name='restaurant-detail'),
    path('restaurants/<int:pk>/update/', views.RestaurantUpdateView.as_view(), name='restaurant-update'),
    path('restaurants/<int:pk>/delete/', views.RestaurantDeleteView.as_view(), name='restaurant-delete'),

    # address
    path('address/', views.AddressListView.as_view(), name='address-list'),
    path('address/create/', views.AddressCreateView.as_view(), name='address-create'),
    path('address/<int:pk>/', views.AddressDetailView.as_view(), name='address-detail'),
    path('address/<int:pk>/update/', views.AddressUpdateView.as_view(), name='address-update'),
    path('address/<int:pk>/delete/', views.AddressDeleteView.as_view(), name='address-delete'),
]
