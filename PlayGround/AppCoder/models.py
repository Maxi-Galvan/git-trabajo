from django.db import models

# Create your models here.
class Tarea(models.Model):
    nombre = models.TextField(max_length=100)
    estado = models.TextField(max_length=100, default='Por_hacer')
    creado_el =models.DateTimeField(auto_now_add = True)
    modifcado_el = models.DateTimeField(auto_now = True)    

def terminar(self):
    self.estado = 'Terminado'


def __str__(self):
    return f'{self.id} - {self.nombre}'

    