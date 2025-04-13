import django_filters

from api.models import Dish


class DishFilter(django_filters.FilterSet):
    name = django_filters.CharFilter(lookup_expr='icontains')
    price = django_filters.NumberFilter(lookup_expr='lte')

    class Meta:
        model = Dish
        fields = ['name', 'price']
