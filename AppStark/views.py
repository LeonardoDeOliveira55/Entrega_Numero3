from django.shortcuts import render
from django.http import HttpResponse, HttpRequest
from .models import *
from .forms import *
# Create your views here.

def inicio (req):
    return render(req, "inicio.html")

def servicios (req):
    
    lista = Contratacion.objects.all()
    
    return render(req, "servicios.html",{"lista_contrataciones" : lista})

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
        form = Presupuesto(req.POST)
        if form.is_valid(): 
            data_formulario = form.cleaned_data
            registro = Contratacion( Lugar_evento= data_formulario["Lugar_evento"], Fecha_evento= data_formulario["Fecha_evento"])
            registro.save()
            return render(req, "inicio.html")
    else:
        form = Presupuesto()
        return render(req, "formulario.html", {"miFormulario": form})
    
def BusquedaServicio (req):
    return render(req, "BusquedaServicios.html")

def Buscar (req: HttpRequest):
    
    if req.GET['Nombre_Servicio']:
        servicio = req.GET['Nombre_Servicio']
        nombre_servicio = Servicios.objects.filter(ID_Servicio__icontains = servicio)
        return render(req, "Resultadobusqueda.html", {"servicios": nombre_servicio})
    
    else:
        return HttpResponse(f"No existe")