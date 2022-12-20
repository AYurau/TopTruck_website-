from django.shortcuts import render


# Create your views here.

def index(request):
    return render(request, 'main/home.html')


def sales(request):
    return render(request, 'main/sales.html')


def bv115(request):
    return render(request, 'main/bv115.html')


def cart(request):
    return render(request, 'main/cart.html')


def offer(request):
    return render(request, 'main/offer.html')


def options(request):
    return render(request, 'main/options.html')


def spare(request):
    return render(request, 'main/spare.html')


def rent(request):
    return render(request, 'main/rent.html')
