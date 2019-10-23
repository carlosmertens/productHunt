from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import auth


def signup(request):
    if request.method == 'POST':
        # User has info and wants an account now!
        if request.POST['password1'] == request.POST['password2']:
            try:
                user = User.objects.get(username=request.POST['username'])
                return render(request, 'accountApp/signup.html', {'error': 'Username is already taken!'})
            except User.DoesNotExist:
                user = User.objects.create_user(
                    request.POST['username'], password=request.POST['password1'])
                auth.login(request, user)
                return redirect('home')
        else:
            return render(request, 'accountApp/signup.html', {'error': 'Passwords does not match!'})
    else:
        # User wants to enter info
        return render(request, 'accountApp/signup.html')


def login(request):
    return render(request, 'accountApp/login.html')


def logout(request):
    # TODO: Route it to home page
    return render(request, 'accountApp/logout.html')
