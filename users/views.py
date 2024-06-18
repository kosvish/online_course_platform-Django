from django.shortcuts import render, reverse, HttpResponseRedirect
from .forms import UserRegistrationForm, UserLoginForm
from django.contrib.auth import authenticate
from django.contrib import auth, messages
from django.contrib.auth.decorators import login_required


def registration(request):
    if request.method == "POST":
        form = UserRegistrationForm(data=request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Вы успешно зарегестрировались')
            return HttpResponseRedirect(reverse('users:login'))
    else:
        form = UserRegistrationForm()
    return render(request, 'users/registration.html', context={"request": request, 'form': form})


def login(request):
    if request.method == "POST":
        
        form = UserLoginForm(data=request.POST)
        if form.is_valid():
            username = request.POST['username']
            password = request.POST['password']
            user = authenticate(username=username, password=password)
            if user:
                auth.login(request, user)
                return HttpResponseRedirect(reverse('main'))
    else:
        form = UserLoginForm()
        return render(request,'users/login.html', context={'request': request, 'form': form})


@login_required
def profile(request):
    return render(request, 'users/profile.html')
