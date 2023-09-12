from django.shortcuts import render
from django.http import HttpResponse
from .models import Servicios
# Create your views here.


def Listar_servicios(req):
    lista = Servicios.objects.all()
    
    return render(req, "Lista_servicios.html",{"lista_servicios" : lista})