from django import forms

class Presupuesto (forms.Form):
    
    Fecha_evento = forms.DateField(help_text="AAAA-MM-DD")
    Lugar_evento = forms.CharField(max_length=50)
    