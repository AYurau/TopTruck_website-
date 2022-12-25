from django.shortcuts import render

# Create your views here.
from main.models import ForSale


def index(request):
    return render(request, 'main/home.html')


def used_machines(request):
    machine_options = {}
    used_machines_models = ForSale.objects.all()
    for machines in used_machines_models:
        machin_options_str = machines.options
        machin_options_lst = []
        for i in machin_options_str.split(','):
            opt = i.strip().capitalize()
            machin_options_lst.append(opt)
        else:
            machine_options[machines.title] = machin_options_lst
    else:
        return render(request, 'main/used_machines.html', {'used_machines_models': used_machines_models,
                                                           'machine_options': machine_options})


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
