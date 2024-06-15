from django.shortcuts import render
from .forms import UserRegistrationForm, UserLoginForm


def registration(request):
    form = UserRegistrationForm()
    return render(request, 'users/registration.html', context={"request": request, 'form': form})


def login(request):
    form = UserLoginForm()
    return render(request, 'users/login.html', context={'request': request, 'form': form})