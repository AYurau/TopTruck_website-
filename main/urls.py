from django.urls import path

from main import views

urlpatterns = [
    path('', views.index),
    path('home.html', views.index),
    path('used_machines.html', views.used_machines),
    path('rent.html', views.rent),
    path('bv115.html', views.bv115),
    path('cart.html', views.cart),
    path('offer_<int:card_id>.html', views.offer, name='card'),
    path('options.html', views.options),
    path('refurbished_chassis.html', views.ref),
    path('fullref.html', views.fullref),
    path('passenger_cabin.html',views.passenger_cabine),
    path('with_board.html', views.with_board),
    path('with_board_crane.html',views.with_board_and_crane),
    path('Engine_Transmitions.html',views.engine_transmition),
    path('brake.html',views.brake),
    path('body.html', views.body),
    path('chassis.html',views.chassis),
    path('electrical.html', views.electrical),
    path('steering.html',views.steering),
    path('other.html',views.other),
    path('spare_<int:spare_id>.html', views.spare, name='sp_card')
]