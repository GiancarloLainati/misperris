from django.db import models
from django.utils import timezone
from PIL import Image
from django import forms

class Rescatado(models.Model):
    author = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    fotografia = models.ImageField()
    nombre = models.CharField(max_length=20)
    raza = models.CharField(max_length=30)
    descripcion = models.TextField()

    ESTADOS_CHOICES = (
        ('rescatado','Rescatado'),
        ('disponible', 'Disponible'),
        ('adoptado','Adoptado'),
        )

    estado = models.CharField(max_length=10, choices=ESTADOS_CHOICES, default='rescatado')

    created_date = models.DateTimeField(
                default=timezone.now)
    published_date = models.DateTimeField(
            blank=True, null=True)


    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.nombre

class Formulario(models.Model):
    email = models.EmailField()
    run = models.IntegerField(primary_key=True)
    dv = models.CharField(max_length=1)
    nombre = models.CharField(max_length=50)
