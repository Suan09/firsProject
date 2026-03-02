from django.db import models

from users.models import User



class Brand(models.Model):
    name = models.CharField(max_length=100)

    class Meta:
        verbose_name = 'Марка автомобиля'
        verbose_name_plural = 'Марки автомобиля'
        

    def __str__(self):
        return f'{self.name}'


class CarModel(models.Model):
    name = models.CharField(max_length=100)
    brand = models.ForeignKey(Brand, on_delete=models.CASCADE)
    class Meta:
        verbose_name = 'Модель автомобиля'
        verbose_name_plural = 'Модели автомобилей'

    def __str__(self):
        return f'{self.name}'

    

class Transmission(models.Model):
    name = models.CharField(max_length=100)

    class Meta:
        verbose_name = 'Коробка передач'

    def __str__(self):
        return f'{self.name}'


class Fuel(models.Model):
    name = models.CharField(max_length=100)

    class Meta:
        verbose_name = 'Топливо'

    def __str__(self):
        return f'{self.name}'

class Color(models.Model):
    name = models.CharField(max_length=100)


class Car(models.Model):
    brand = models.ForeignKey(Brand, on_delete=models.CASCADE)
    model = models.ForeignKey(CarModel, on_delete=models.CASCADE)
    transmission = models.ForeignKey(Transmission, on_delete=models.CASCADE)
    fuel = models.ForeignKey(Fuel, on_delete=models.CASCADE)
    color = models.ForeignKey(Color, on_delete=models.CASCADE, blank=True, null=True)
    price = models.PositiveIntegerField(default=0)
    mileage = models.PositiveIntegerField(default=0)
    year = models.PositiveIntegerField(default=0)
    description = models.TextField(max_length=1000, default='')
    image = models.ImageField(upload_to='cars', verbose_name='Изображение', blank=True, null=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='Владелец', null=True)

    class Meta:
        verbose_name = 'Машина'
        verbose_name_plural = 'Машины'

    def __str__(self):
        return f'{self.model.name}'
