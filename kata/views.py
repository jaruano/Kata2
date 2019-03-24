from django.shortcuts import render, get_list_or_404
from django.http import HttpResponse,JsonResponse,Http404
from .models import Portafolio, Imagen
from django.core import serializers
import json
from django.contrib.auth.models import User
from django.db.models import Q

def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")

def getPortafolios(request):
    portafolios = Portafolio.objects.all()
    return HttpResponse(serializers.serialize('json',portafolios))

def usuarios(request):
    if(request.method == 'POST'):
        jsonUser = json.loads(request.body)
        userName = jsonUser['username']
        firstName = jsonUser['first_name']
        lastName = jsonUser['last_name']
        password = jsonUser['password']
        email = jsonUser['email']

        userModel = User.objects.create_user(username = userName, password=password)
        userModel.first_name=firstName
        userModel.last_name=lastName
        userModel.email=email
        userModel.save()

        return HttpResponse(serializers.serialize('json',[userModel]))
    return Http404()

def portafoliosPublicos(request, id):
    imagenes = get_list_or_404(Imagen, Q(relatedPortafolio_id = id) & Q(isPublic = True))
    return HttpResponse(serializers.serialize('json',imagenes))
