from django.contrib import admin

from . import models

admin.site.register(models.Dish)
admin.site.register(models.Order)
admin.site.register(models.Address)
admin.site.register(models.Restaurant)
