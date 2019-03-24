from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('portafolios', views.getPortafolios, name='getPortafolios'),
    path('usuarios', views.usuarios, name='usuarios'),
]