from django.db import models
from django.contrib.auth.models import AbstractUser 

from phonenumber_field.modelfields import PhoneNumberField


class User(AbstractUser):
    username = models.CharField(max_length=100, unique=True)
    phone = PhoneNumberField(unique=True, verbose_name='Номер телефона')

    class Meta:
        db_table = 'users'
        verbose_name = 'Пользователю'
        verbose_name_plural = 'Пользователи'

    def __str__(self):
        return f'{self.username}'
    
