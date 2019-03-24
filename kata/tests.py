from django.test import TestCase
import json
from django.contrib.auth.models import User
from .models import Portafolio

# Create your tests here.
class KataTestCase(TestCase):
    def testPaso1ListaPortafolios200(self):
        url='/api/portafolios'
        response =  self.client.get(url, format='json')
        self.assertEqual(response.status_code , 200)

    def testPaso2ListaPortafoliosElementosEspecificos(self):
        userModel = User.objects.create_user(username="test", password="test", first_name="test", last_name="test", email="test@test.com")
        portafolio = Portafolio.objects.create(propietario=userModel)
        url='/api/portafolios'
        response =  self.client.get(url, format='json')
        portafolios = json.loads(response.content)
        self.assertEqual(len(portafolios), 1)