from django.shortcuts import render
from django.http import HttpResponse, HttpRequest
from .models import *
from .forms import *
# Create your views here.

def inicio (req):
    return render(req, "inicio.html")

def servicios (req):
    
    return render(req, "servicios.html")

def registro (req):
    
    return render(req, "registro_clientes.html")


def Listar_servicios(req):
    lista = Servicios.objects.all()
    
    return render(req, "Lista_servicios.html",{"lista_servicios" : lista})

def Listar_clientes(req):
    lista = Lista_Clientes.objects.all()
    
    return render(req, "Lista_clientes.html",{"lista_clientes" : lista})

def formulario (req):
    if req.method == 'POST':
        miFormulario = Presupuesto(req.POST)
        if miFormulario.is_valid(): 
            data_formulario = Presupuesto.cleaned_data
            registro = Contratacion( Lugar_evento= data_formulario["Direccion"], Fecha_evento= data_formulario["Fecha del Servicios"])
            registro.save()
        return render(req, "inicio.html")
    else:
        miFormulario = Presupuesto()
        return render(req, "formulario.html", {"miFormulario": miFormulario})
    
def BusquedaServicio (req):
    return render(req, "BusquedaServicios.html")

def Buscar (req: HttpRequest):
    
    if req.GET['Nombre_Servicio']:
        servicio = req.GET['Nombre_Servicio']
        nombre_servicio = Servicios.objects.get(Nombre_Servicio = servicio)
        return render(req, "Resultadobusqueda.html", {"servicios": nombre_servicio})
    
    else:
        return HttpResponse(f"No existe")