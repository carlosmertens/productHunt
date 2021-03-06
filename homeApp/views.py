from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Product
from django.utils import timezone


def home(request):
    products = Product.objects
    return render(request, 'homeApp/index.html', {'products': products})


@login_required(login_url='/accountApp/signup')
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

        return redirect('/product/' + str(product.id))

    else:
        return render(request, 'homeApp/create.html')


def detail(request, product_id):
    product = get_object_or_404(Product, pk=product_id)
    return render(request, 'homeApp/detail.html', {'product': product})


@login_required(login_url='/accountApp/signup')
def upvote(request, product_id):
    if request.method == 'POST':
        product = get_object_or_404(Product, pk=product_id)
        product.votes_total += 1
        product.save()
        return redirect('/product/' + str(product.id))
