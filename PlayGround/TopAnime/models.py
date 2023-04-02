from django.db import models

# Create your models here.
class anime(models.Model):
    nombre_principal = models.CharField(max_length=30)
    cantidad_de_temporadas = models.CharField(max_length=3)
    descripcion = models.CharField(max_length=200)


    def __str__(self):
        return f"{self.id} - {self.nombre_principal} - {self.cantidad_de_temporadas} - {self.descripcion}"
