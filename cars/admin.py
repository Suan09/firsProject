from django.contrib import admin

from cars.models import Brand, Car, CarModel, Fuel, Transmission



admin.site.register(Brand)
admin.site.register(CarModel)
admin.site.register(Transmission)
admin.site.register(Fuel)
admin.site.register(Car)
