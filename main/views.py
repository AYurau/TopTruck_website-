from django.shortcuts import render, get_object_or_404

# Create your views here.
from main.models import ForSale, Details
from cart.forms import CartAddProductForm


def index(request):
    return render(request, 'main/home.html')


def passenger_cabine(request):
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
        return render(request, 'main/passenger_cabin.html', {'used_machines_models': used_machines_models,
                                                             'machine_options': machine_options})


def with_board(request):
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
        return render(request, 'main/with_board.html', {'used_machines_models': used_machines_models,
                                                        'machine_options': machine_options})


def engine_transmition(request):
    machine_options = {}
    used_machines_models = Details.objects.all()
    for machines in used_machines_models:
        machin_options_str = machines.options
        machin_options_lst = []
        for i in machin_options_str.split(','):
            opt = i.strip().capitalize()
            machin_options_lst.append(opt)
        else:
            machine_options[machines.title] = machin_options_lst
    else:
        return render(request, 'main/Engine_Transmitions.html', {'used_machines_models': used_machines_models,
                                                                 'machine_options': machine_options})


def brake(request):
    machine_options = {}
    used_machines_models = Details.objects.all()
    for machines in used_machines_models:
        machin_options_str = machines.options
        machin_options_lst = []
        for i in machin_options_str.split(','):
            opt = i.strip().capitalize()
            machin_options_lst.append(opt)
        else:
            machine_options[machines.title] = machin_options_lst
    else:
        return render(request, 'main/brake.html', {'used_machines_models': used_machines_models,
                                                   'machine_options': machine_options})


def body(request):
    machine_options = {}
    used_machines_models = Details.objects.all()
    for machines in used_machines_models:
        machin_options_str = machines.options
        machin_options_lst = []
        for i in machin_options_str.split(','):
            opt = i.strip().capitalize()
            machin_options_lst.append(opt)
        else:
            machine_options[machines.title] = machin_options_lst
    else:
        return render(request, 'main/body.html', {'used_machines_models': used_machines_models,
                                                  'machine_options': machine_options})


def chassis(request):
    machine_options = {}
    used_machines_models = Details.objects.all()
    for machines in used_machines_models:
        machin_options_str = machines.options
        machin_options_lst = []
        for i in machin_options_str.split(','):
            opt = i.strip().capitalize()
            machin_options_lst.append(opt)
        else:
            machine_options[machines.title] = machin_options_lst
    else:
        return render(request, 'main/chassis.html', {'used_machines_models': used_machines_models,
                                                     'machine_options': machine_options})


def electrical(request):
    machine_options = {}
    used_machines_models = Details.objects.all()
    for machines in used_machines_models:
        machin_options_str = machines.options
        machin_options_lst = []
        for i in machin_options_str.split(','):
            opt = i.strip().capitalize()
            machin_options_lst.append(opt)
        else:
            machine_options[machines.title] = machin_options_lst
    else:
        return render(request, 'main/electrical.html', {'used_machines_models': used_machines_models,
                                                              'machine_options': machine_options})


def steering(request):
    machine_options = {}
    used_machines_models = Details.objects.all()
    for machines in used_machines_models:
        machin_options_str = machines.options
        machin_options_lst = []
        for i in machin_options_str.split(','):
            opt = i.strip().capitalize()
            machin_options_lst.append(opt)
        else:
            machine_options[machines.title] = machin_options_lst
    else:
        return render(request, 'main/steering.html', {'used_machines_models': used_machines_models,
                                                              'machine_options': machine_options})


def other(request):
    machine_options = {}
    used_machines_models = Details.objects.all()
    for machines in used_machines_models:
        machin_options_str = machines.options
        machin_options_lst = []
        for i in machin_options_str.split(','):
            opt = i.strip().capitalize()
            machin_options_lst.append(opt)
        else:
            machine_options[machines.title] = machin_options_lst
    else:
        return render(request, 'main/other.html', {'used_machines_models': used_machines_models,
                                                              'machine_options': machine_options})


def with_board_and_crane(request):
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
        return render(request, 'main/with_board_crane.html', {'used_machines_models': used_machines_models,
                                                              'machine_options': machine_options})


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
    return render(request, 'main/offer.html', {'obj': obj,
                                               'machine_options': machine_options})


def options(request):
    return render(request, 'main/options.html')


def spare(request):
    return render(request, 'main/Engine_Transmitions.html')


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
