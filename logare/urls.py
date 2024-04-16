from django.urls import path
from .views import paginaLogare, delogareUtilizator


urlpatterns = [
    path('login/', paginaLogare, name = 'login'),
    path('logout/', delogareUtilizator, name = 'logout'),
]
