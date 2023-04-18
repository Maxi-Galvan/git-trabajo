from django.shortcuts import render
from Top_Series.models import Serie, Comentarios,Proximas_Series
from Top_Series.form import FormularioSerie, FormularioComentarios, FormularioFuturosLanzamientos, BuscarSerie
from django.views.generic import ListView

def mostrar_contenido(request):
    series = Serie.objects.all()
    coments= Comentarios.objects.all()
    prox_lanzamientos = Proximas_Series.objects.all()

    context = {
        'series': series,
        'comentarios': coments,
        'prox_lanzamientos': prox_lanzamientos,
    }

    return render(request, 'Top_Series/contenido.html', context)




def cargar_serie(request):

    f = FormularioSerie(request.POST)
    series = Serie.objects.all()
   
    
    context = {
        'series': series,
        'form': f,
    }
    
    if f.is_valid():
        
        Serie(nombre = f.data['nombre'], 
        cant_temp = f.data['cant_temp'],
        resumen = f.data['resumen'],
        puntaje = f.data['puntaje']).save()

    return render(request, 'Top_Series/formulario_carga_serie.html', context)




def cargar_comentario(request):

    f = FormularioComentarios(request.POST)
    Coment = Comentarios.objects.all()
    
    context = {
        'comentario': Coment,
        'form': f,
    }

    if f.is_valid():
        
        Comentarios(nombre_usuario = f.data['nombre_usuario'], texto = f.data['texto']).save()

    return render(request, 'Top_Series/formulario_carga_comentario.html', context)



def cargar_lanzamiento(request):

    f = FormularioFuturosLanzamientos(request.POST)
    prox_series = Proximas_Series.objects.all()
    
    context = {
        'nombre_serie': prox_series,
        'form': f,
    }

    if f.is_valid():
        
        Proximas_Series(nombre_proxima_serie = f.data['nombre_proxima_serie'], fecha_lanzamiento = f.data['fecha_lanzamiento']).save()

    return render(request, 'Top_Series/formulario_carga_futuros_lanzamientos.html', context)
    


class Buscar_Serie(ListView):
    model = Serie
    template_name = 'serie_list.html'
    context_object_name = 'Series'

    def get_queryset(self):
        
        f = BuscarSerie(self.request.GET)

        if f.is_valid():
            return Serie.objects.filter(nombre__icontains=f.data['criterio_nombre']).all()
        
        return Serie.objects.none()


 