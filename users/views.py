"""Users app views"""

from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect


def signin(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, password=password, username=username)

        if user:
            login(request, user)
            return redirect('generator:identicon')

    return render(request, 'users/signin.html')


def signup(request):
    if request.method == 'POST':
        data = {
            'username': request.POST.get('username'),
            'email': request.POST.get('email'),
            'password': request.POST.get('password'),
        }
        user = User.objects.create_user(**data)
        login(request, user)
        return redirect('generator:identicon')

    return render(request, 'users/signup.html')


@login_required
def signoff(request):
    logout(request)
    return redirect('users:signin')
