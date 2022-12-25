from django.urls import path

from main import views

urlpatterns = [
    path('', views.index),
    path('home.html', views.index),
    path('used_machines.html', views.used_machines),
    path('rent.html', views.rent),
    path('bv115.html', views.bv115),
    path('cart.html', views.cart),
    path('offer.html', views.offer),
    path('options.html', views.options),
    path('spare.html', views.spare),
]