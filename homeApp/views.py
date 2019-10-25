from django.shortcuts import render
from django.contrib.auth.decorators import login_required


def home(request):
    return render(request, 'homeApp/index.html')


@login_required
def create(request):
    return render(request, 'homeApp/create.html')
