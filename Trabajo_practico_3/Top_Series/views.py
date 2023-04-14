from django.shortcuts import render
from Top_Series.models import Serie
from Top_Series.form import FormularioSerie

def mostrar_serie(request):
    series = Serie.objects.all()
    return render(request, 'Top_Series/index.html', {'series': series})


def cargar_serie(request):
    f = FormularioSerie(request.POST)
    series = Serie.objects.all()
    total_cantidad_series = len(series)
    
    context = {
        'series': series,
        'total_cantidad_series': total_cantidad_series,
        'form': f,
    }
    
    if f.is_valid():
        
        Serie(nombre = f.data['nombre'], 
        cant_temp = f.data['cant_temp'],
        resumen = f.data['resumen'],
        puntaje = f.data['puntaje']).save()

    return render(request, 'Top_Series/formulario.html', context)