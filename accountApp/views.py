from django.shortcuts import render


def signup(request):
    return render(request, 'accountApp/signup.html')


def login(request):
    return render(request, 'accountApp/login.html')


def logout(request):
    # TODO: Route it to home page
    return render(request, 'accountApp/logout.html')
