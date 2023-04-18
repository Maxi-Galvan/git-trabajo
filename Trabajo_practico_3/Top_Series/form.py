from django import forms

class FormularioSerie(forms.Form):
    nombre = forms.CharField(max_length=50)
    cant_temp = forms.CharField(max_length=10)
    resumen = forms.CharField(max_length=500)
    puntaje = forms.CharField(max_length= 10)



class FormularioComentarios(forms.Form):
    nombre_usuario = forms.CharField(max_length=50)
    texto = forms.CharField(max_length=500)


class FormularioFuturosLanzamientos(forms.Form):
    nombre_proxima_serie = forms.CharField(max_length=50)
    fecha_lanzamiento = forms.CharField(max_length=20)


class BuscarSerie(forms.Form):
    criterio_nombre = forms.CharField(max_length=50)
    

