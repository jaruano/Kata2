from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Portafolio(models.Model):
    propietario = models.ForeignKey(User, on_delete=models.CASCADE)



class Imagen(models.Model):
    titulo = models.CharField(max_length=200)
    url = models.CharField(max_length=1000)
    description = models.CharField(max_length=1000,null=True)
    type = models.CharField(max_length=3,blank=True)
    isPublic = models.BooleanField(default=False)
    relatedPortafolio = models.ForeignKey(Portafolio, on_delete=models.CASCADE)

