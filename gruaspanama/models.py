from django.db import models
from django.utils.html import format_html

# Esta clase representa a una maquina de la seccion de alquiler-online.

class Maquina(models.Model):
    modelo               = models.CharField(max_length=20, blank=True, null=True)
    imagen               = models.ImageField(upload_to="maquina/%Y/%m/%d", default='defecto/defecto.png', blank=True, null=True)
    marca                = models.CharField(max_length=20, blank=True)
    segmento             = models.CharField(max_length=20, blank=True)
    año                  = models.DateField(blank=True, null=True)
    capacidad            = models.CharField(max_length=3, blank=True)
    pluma                = models.CharField(max_length=3, blank=True)
    plumin               = models.CharField(max_length=3, blank=True)
    potencia             = models.CharField(max_length=10, blank=True)
    disponible           = models.BooleanField(blank=True)

    def __str__(self, ):
        return self.modelo
