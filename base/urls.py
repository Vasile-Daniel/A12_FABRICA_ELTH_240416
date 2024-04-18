from django.urls import path
from .views import homeFabrica, plaseazaComanda
urlpatterns = [
    path('', homeFabrica, name = 'home' ),
    path('plaseaza_comanda/', plaseazaComanda, name = 'plaseaza_comanda'),
]
