from django.test import TestCase, Client
from myapp.views import sumar

# Test del endpoint ping
class PingTests(TestCase):
    def setUp(self):
        self.client = Client()

    def test_endpoint_ping_responde_con_pong(self):
        response = self.client.get('/ping/')
        self.assertEqual(response.status_code, 200)
        self.assertJSONEqual(response.content, {'ping': 'pong'})

# Test de la función sumar
class SumaTests(TestCase):
    def test_sumar_dos_numeros_ok(self):
        self.assertEqual(sumar(2, 2), 4)
    def test_sumar_dos_numeros_negativos(self):
        self.assertEqual(sumar(-2, -2), -4)
    def test_sumar_un_numero_negativo_y_uno_positivo(self):
        self.assertEqual(sumar(-2, 2), 0)
