from django.db import models
from django.contrib.auth.models import User

class juegos(models.Model):
    nombre = models.TextField (max_length=30)
    descripcion = models.TextField (max_length=100)
    publisher = models.ForeignKey(to=User, on_delete=models.CASCADE, related_name='publisher')

    def __str__(self):
        return f'{self.id} -- {self.nombre} -- {self.descripcion}'

    