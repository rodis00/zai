from django.contrib.auth.models import User
from django.db import models


class Restaurant(models.Model):
    name = models.CharField(max_length=255)
    owner = models.OneToOneField(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class Address(models.Model):
    city = models.CharField(max_length=120)
    country = models.CharField(max_length=120)
    street = models.CharField(max_length=120, null=True)
    zipcode = models.CharField(max_length=120)
    restaurant = models.OneToOneField(Restaurant, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.city}, {self.country} ({self.zipcode})"


class Dish(models.Model):
    restaurant = models.ForeignKey(Restaurant, on_delete=models.CASCADE, related_name='dishes')
    name = models.CharField(max_length=255)
    price = models.DecimalField(decimal_places=2, max_digits=6)
    description = models.TextField()
    picture = models.ImageField(upload_to='dish_pictures')

    def __str__(self):
        return f"{self.name} ({self.restaurant.name})"


PAYMENT_CHOICES = (
    ('CC', 'CREDIT_CARD'),
    ('B', 'BLIK'),
    ('C', 'CASH')
)


class Order(models.Model):
    customer = models.ForeignKey(User, on_delete=models.CASCADE, related_name='orders')
    dishes = models.ManyToManyField(Dish)
    payment = models.CharField(choices=PAYMENT_CHOICES, max_length=2)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Order #{self.id} by {self.customer.username}"
