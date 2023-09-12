from django.db import models

# Create your models here.

class Servicios (models.Model):
    Nombre_Servicio = models.CharField(max_length=40)
    Tipo_Servicio = models.CharField(max_length=20)
    ID_Servicio = models.IntegerField()
    
    def __str__(self):
        return f'{self.Nombre_Servicio} - {self.Tipo_Servicio} - {self.ID_Servicio}'
    
    class Meta():
        verbose_name = 'Servicio'
        verbose_name_plural = 'Servicios'
        ordering = ('Nombre_Servicio',)
    
class Lista_Clientes (models.Model):
    Nombre_Cliente = models.CharField(max_length=40)
    DNI_Cliente = models.IntegerField()
    Numero_contacto = models.IntegerField()
    
    def __str__(self):
        return f'{self.Nombre_Cliente}'
    
    class Meta():
        verbose_name = 'Lista Clientes'
        verbose_name_plural = 'Lista Clientes'
        ordering = ('Nombre_Cliente',)
    
class Contratacion (models.Model):
    Fecha_evento = models.DateField()
    Lugar_evento = models.CharField(max_length=50)
    Seña = models.BooleanField(default= False)
    
    def __str__(self):
        return f'{self.Fecha_evento} / {self.Lugar_evento}'
    
    class Meta():
        verbose_name = 'Contratacion'
        verbose_name_plural = 'Contrataciones'
        ordering = ('Fecha_evento',)
    
    
    
    