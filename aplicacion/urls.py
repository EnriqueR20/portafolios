
from django.urls import path,include
from . import views

urlpatterns = [
    path('', views.inicio, name='aplicacion'),
    path('login/', views.logeador, name='logeador'),
    path('registrar/', views.registrar, name='registrar'),
    path('proyectos/', views.proyectos, name='proyectos'),
    path('', views.salir, name='salir'),

]