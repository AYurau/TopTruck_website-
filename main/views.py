from django.shortcuts import render, get_object_or_404

# Create your views here.
from main.models import ForSale
from cart.forms import CartAddProductForm


def index(request):
    return render(request, 'main/home.html')


def fullref(request):
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
        return render(request, 'main/fullref.html', {'used_machines_models': used_machines_models,
                                                     'machine_options': machine_options})


def ref(request):
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
        return render(request, 'main/refurbished_chassis.html', {'used_machines_models': used_machines_models,
                                                                 'machine_options': machine_options})


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
    return render(request, 'cart/detail.html')


def offer(request, card_id):
    obj = ForSale.objects.get(pk=card_id)
    machine_options = {}
    machin_options_str = obj.options
    machin_options_lst = []
    for i in machin_options_str.split(','):
        opt = i.strip().capitalize()
        machin_options_lst.append(opt)
    else:
        machine_options[obj.title] = machin_options_lst
    return render(request, 'main/offer.html',{'obj':obj,
                                              'machine_options':machine_options})


def options(request):
    return render(request, 'main/options.html')


def spare(request):
    return render(request, 'main/spare.html')


def rent(request):
    return render(request, 'main/rent.html')


def product_detail(request, id, slug):
    product = get_object_or_404(ForSale,
                                id=id,
                                slug=slug,
                                available=True)
    cart_product_form = CartAddProductForm()
    return render(request, 'cart/detail.html', {'product': product,
                                                        'cart_product_form': cart_product_form})
