from django.test import TestCase, Client
from myapp.views import sumar

# Test del endpoint ping
class PingTests(TestCase):
    def setUp(self):
        self.client = Client()

    def test_ping(self):
        response = self.client.get('/ping/')
        self.assertEqual(response.status_code, 200)
        self.assertJSONEqual(response.content, {'ping': 'pong'})

# Test de la función sumar
class SumaTests(TestCase):
    def test_sumar(self):
        self.assertEqual(sumar(2, 2), 4)
