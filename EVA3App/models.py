from django.db import models

# Create your models here.

class Reserva(models.Model):
    nombre = models.CharField(max_length=50)
    telefono = models.IntegerField()
    fecha = models.DateField(null=True, blank=True)
    hora= models.TimeField()
    cantidadPersonas= models.IntegerField()
    estado = models.CharField(max_length=50)
    observacion = models.CharField(max_length=100)