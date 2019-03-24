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

    def testPaso2ListaPortafolios2Elementos(self):
        userModel = User.objects.create_user(username="test", password="test", first_name="test", last_name="test",
                                             email="test@test.com")
        userModel2 = User.objects.create_user(username="test2", password="test2", first_name="test2", last_name="test2",
                                             email="test2@test.com")
        portafolio = Portafolio.objects.create(propietario=userModel)
        portafolio2 = Portafolio.objects.create(propietario=userModel2)
        url = '/api/portafolios'
        response = self.client.get(url, format='json')
        portafolios = json.loads(response.content)

        self.assertEqual(len(portafolios), 2)

    def testPaso3RegistrarUsuario(self):
        url = '/api/usuarios'
        response = self.client.post(url, json.dumps({"username":"utest", "password":"utest", "first_name":"utest", "last_name":"utest", "email":"utest@test.com"}), content_type='application/json')
        self.assertEqual(response.status_code, 201)
        currentData = json.loads(response.content)
        self.assertEqual(currentData[0]['fields']['username'], "utest")