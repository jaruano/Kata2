from django.test import TestCase

# Create your tests here.
class KataTestCase(TestCase):
    def testPaso1ListaPortafolios200(self):
        url='/api/portafolios'
        response =  self.client.get(url, format='json')
        self.assertEqual(response.status_code , 200)