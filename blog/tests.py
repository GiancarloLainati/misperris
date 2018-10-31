import unittest
from django.test import Client
from .models import Rescatado
from django.utils import timezone

# Para ejecutar el test colocar python manage.py test

class SimpleTest(unittest.TestCase):
   def setUp(self):
       # Todo test necesita un cliente.
       self.client = Client()

   def test_details_login(self):
       # Se emite una solicitud GET.
       response = self.client.get('/login/')

       # Se comprueba que la respuesta es 200.
       self.assertEqual(response.status_code, 200)
  
   def test_details_signup(self):
       # Se emite una solicitud GET.
       response = self.client.get('/signup/')

       # Se comprueba que la respuesta es 200.
       self.assertEqual(response.status_code, 200)

   def test_details_rescatados(self):
       # Se emite una solicitud GET.
       response = self.client.get('/rescatados/')

       # Se comprueba que la respuesta es 200.
       self.assertEqual(response.status_code, 200)

   def test_details_password_reset(self):
       # Se emite una solicitud GET.
       response = self.client.get('/password_reset/')

       # Se comprueba que la respuesta es 200.
       self.assertEqual(response.status_code, 200)