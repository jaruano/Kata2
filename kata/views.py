from django.shortcuts import render
from django.http import HttpResponse,JsonResponse
from .models import Portafolio
from django.core import serializers

def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")

def getPortafolios(request):
    portafolios = Portafolio.objects.all()
    return HttpResponse(serializers.serialize('json',portafolios))