from django import forms

class Presupuesto (forms.Form):
    
    Fecha_evento = forms.DateField()
    Lugar_evento = forms.CharField(max_length=50)
    