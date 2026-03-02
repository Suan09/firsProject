from django.shortcuts import render, redirect
from django.contrib import auth
from django.contrib import auth, messages
from django.http.response import HttpResponseRedirect
from django.urls import reverse

from users.forms import UserRegistrationForm, UserLoginForm




def registration(request):
    if request.method == 'POST':
        form = UserRegistrationForm(data=request.POST)
        if form.is_valid():
            form.save()
            user = form.instance
            auth.login(request, user)
            messages.success(request, f'{user.username} успешно зарегистрировались')
            return HttpResponseRedirect(reverse('cars:index'))
    else:
        form = UserRegistrationForm()

    return render(request, 'users/registration.html', {'form': form})


def login(request):
    if request.method == 'POST':
        form = UserLoginForm(data=request.POST)

        if form.is_valid():
            username = request.POST.get('username')
            password = request.POST.get('password')
            user = auth.authenticate(username=username, password=password)
            if user:
                auth.login(request, user)
                messages.success(request, f'{username} вы вошли в аккаунт')
                return HttpResponseRedirect(reverse('cars:index'))
    else:
        form = UserLoginForm()

    return render(request, 'users/login.html', {'form': form})


def logout(request):
    auth.logout(request)
    messages.success(request, 'вы вышли из аккаунта')
    return redirect(reverse('cars:index'))    


