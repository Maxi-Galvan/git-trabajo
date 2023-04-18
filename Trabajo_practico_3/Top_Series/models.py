from django.db import models

class Serie(models.Model):
    nombre = models.TextField(max_length=50)
    cant_temp = models.TextField(max_length=3)
    resumen = models.TextField(max_length=100)
    puntaje = models.TextField(max_length=3)


    def __str__(self):
        return f"{self.id} - {self.nombre} - {self.cant_temp} - {self.puntaje}"


class Comentarios(models.Model):
    nombre_usuario = models.TextField(max_length=50)
    texto = models.TextField(max_length=500)
    

    def __str__(self):
        return f"{self.id} - {self.nombre_usuario} - {self.texto}"
    

class Proximas_Series(models.Model):
    nombre_proxima_serie = models.TextField(max_length=50)
    fecha_lanzamiento = models.TextField(max_length=20)

    def __str__(self):
        return f"{self.id} - {self.nombre_proxima_serie} - {self.fecha_lanzamiento}"

