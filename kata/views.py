from django.shortcuts import render
from django.http import HttpResponse,JsonResponse,Http404
from .models import Portafolio
from django.core import serializers
import json
from django.contrib.auth.models import User

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
