from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('portafolios', views.getPortafolios, name='getPortafolios'),
    path('usuarios', views.usuarios, name='usuarios'),
    path('usuarios/<int:id>', views.usuariosId, name='usuariosId'),
    path('portafolios/<int:id>/publico', views.portafoliosPublicos, name='portafoliosPublicos'),
    path('usuarios/login', views.usuariosLogin, name='usuariosLogin'),
]