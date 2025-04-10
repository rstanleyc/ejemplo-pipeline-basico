from django.test import TestCase
from myapp.views import sumar

class SumaTests(TestCase):
    def test_sumar_correctamente(self):
        self.assertEqual(sumar(2, 2), 4)

    def test_sumar_fallando(self):
        self.assertEqual(sumar(2, 2), 5)
