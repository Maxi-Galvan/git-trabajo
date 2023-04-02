from django.shortcuts import render
from AppCoder.models import Tarea 

# Create your views here.
def mostrar_mi_template(request, nombre, apellido):
    context= {
        'nombre': nombre.title(),
        'apellido': apellido.title(),
        'Notas': [5,6,7,8,9],
    }
    return render(request, 'AppCoder/index.html', context)


def mostrar_mis_tareas(request):
    tareas = Tarea.objects.all()
    return render(request, 'AppCoder/tareas.html', {'tareas': tareas})