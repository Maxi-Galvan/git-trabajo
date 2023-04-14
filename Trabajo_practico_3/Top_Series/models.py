from django.db import models

class Serie(models.Model):
    nombre = models.TextField(max_length=50)
    cant_temp = models.TextField(max_length=3)
    resumen = models.TextField(max_length=100)
    puntaje = models.TextField(max_length=3)


    def __str__(self):
        return f"{self.id} - {self.nombre} - {self.cant_temp} - {self.puntaje}"

