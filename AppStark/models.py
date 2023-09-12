from django.db import models

# Create your models here.

class Servicios (models.Model):
    Nombre_Servicio = models.CharField(max_length=40)
    Tipo_Servicio = models.CharField(max_length=20)
    ID_Servicio = models.IntegerField()
    
class Lista_Clientes (models.Model):
    Nombre_Cliente = models.CharField(max_length=40)
    DNI_Cliente = models.IntegerField()
    Numero_contacto = models.IntegerField()
    
class Contratacion (models.Model):
    Fecha_evento = models.DateField()
    Lugar_evento = models.CharField(max_length=50)
    Seña = models.BooleanField()