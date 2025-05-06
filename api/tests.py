from django.test import TestCase
from django.contrib.auth.models import User
from api.models import Restaurant, Address, Dish, Order


class ModelTests(TestCase):

    def setUp(self):
        self.owner = User.objects.create_user(username="owner", password="pass")
        self.customer = User.objects.create_user(username="customer", password="pass")
        self.restaurant = Restaurant.objects.create(
            name="Pizza Heaven", owner=self.owner
        )

    def test_create_restaurant(self):
        self.assertEqual(self.restaurant.name, "Pizza Heaven")
        self.assertEqual(self.restaurant.owner, self.owner)

    def test_create_address(self):
        address = Address.objects.create(
            city="Warsaw",
            country="Poland",
            street="Main Street",
            zipcode="00-001",
            restaurant=self.restaurant,
        )

        self.assertEqual(address.city, "Warsaw")
        self.assertEqual(address.restaurant, self.restaurant)

    def test_create_dish(self):
        dish = Dish.objects.create(
            restaurant=self.restaurant,
            name="Margherita",
            price=25.00,
            description="Classic pizza",
            picture="pizza.jpg",
        )

        self.assertEqual(dish.name, "Margherita")
        self.assertEqual(dish.restaurant, self.restaurant)

    def test_create_order_with_dishes(self):
        dish1 = Dish.objects.create(
            restaurant=self.restaurant,
            name="Kebab",
            price=12.50,
            description="Spicy kebab",
            picture="kebab.jpg",
        )

        dish2 = Dish.objects.create(
            restaurant=self.restaurant,
            name="Falafel",
            price=10.00,
            description="Vegan falafel",
            picture="falafel.jpg",
        )

        order = Order.objects.create(customer=self.customer, payment="CC")
        order.dishes.set([dish1, dish2])

        self.assertEqual(order.dishes.count(), 2)
