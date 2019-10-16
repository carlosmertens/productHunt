from django.shortcuts import render


def home(request):
    return render(request, 'homeApp/index.html')
