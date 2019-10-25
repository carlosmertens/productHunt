from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import Product
from django.utils import timezone


def home(request):
    return render(request, 'homeApp/index.html')


@login_required
def create(request):

    if request.method == 'POST':
        product = Product()
        product.title = request.POST['title']
        product.url = request.POST['url']
        product.image = request.FILES['image']
        product.icon = request.FILES['icon']
        product.body = request.POST['body']
        product.pub_date = timezone.datetime.now()
        product.hunter = request.user

        product.save()

        return redirect('home')

    else:
        return render(request, 'homeApp/create.html')
