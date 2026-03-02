from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django import forms

from phonenumber_field.formfields import PhoneNumberField

from users.models import User


class UserRegistrationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'phone']

    username = forms.CharField()
    phone = PhoneNumberField()
    password1 = forms.PasswordInput()
    password2 = forms.PasswordInput()


class UserLoginForm(AuthenticationForm):
    username = forms.CharField(label="Логин")
    password = forms.PasswordInput()

    class Meta:
        model = User
        fields = ['username', 'password']


