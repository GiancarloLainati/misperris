from django.test import TestCase
from .models import Rescatado
from django.utils import timezone

""" class RescatadoTestCase(TestCase):
    def setUp(self):
        Rescatado.objects.create(fotografia="null", nombre="flor", raza="lola", descripcion="hola", estado="disponible", published_date=timezone.now)
        Rescatado.objects.create(fotografia="null", nombre="pinta", raza="quilter", descripcion="holanda", estado="disponible", published_date=timezone.now)

    def test_rescatado_nombre(self):
        flor = Rescatado.objects.get(nombre="flor")
        pinta = Rescatado.objects.get(nombre="pinta")
        self.assertEqual(flor, 'flor')
        self.assertEqual(pinta, 'pinta') """