from django import forms

class FormularioSerie(forms.Form):
    nombre = forms.CharField(max_length=50)
    cant_temp = forms.CharField(max_length=10)
    resumen = forms.CharField(max_length=500)
    puntaje = forms.CharField(max_length= 10)