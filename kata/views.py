from django.shortcuts import render, get_list_or_404,get_object_or_404
from django.http import HttpResponse,JsonResponse,Http404,HttpResponseForbidden
from .models import Portafolio, Imagen
from django.core import serializers
import json
from django.contrib.auth.models import User
from django.db.models import Q
from django.contrib.auth import authenticate,login

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

def usuariosId(request,id):
    if(request.method == 'PUT'):
        usuario = get_object_or_404(User,id=id)
        if usuario is not None:
            jsonUser = json.loads(request.body)
            firstName = jsonUser['first_name']
            lastName = jsonUser['last_name']
            email = jsonUser['email']

            usuario.first_name = firstName
            usuario.last_name = lastName
            usuario.email = email

            usuario.save()

            return HttpResponse(serializers.serialize('json',[usuario]))
    return Http404()

        

def portafoliosPublicos(request, id):
    imagenes = get_list_or_404(Imagen, Q(relatedPortafolio_id = id) & Q(isPublic = True))
    return HttpResponse(serializers.serialize('json',imagenes))

def usuariosLogin(request):
    if request.method == 'POST':
        jsonUser = json.loads(request.body)
        userName = jsonUser['username']
        password = jsonUser['password']
        user = authenticate(request, username=userName, password=password)
        if user is not None:
            login(request, user)
            return HttpResponse('')

            

    return HttpResponseForbidden()