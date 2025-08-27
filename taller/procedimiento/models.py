from django.db import models
from mecanico.models import Mecanico
from vehiculo.models import Vehiculo

class Procedimiento(models.Model):
    nombre = models.CharField(max_length=100)
    descripcion = models.TextField()
    mecanico = models.ForeignKey(Mecanico, on_delete=models.PROTECT)
    vehiculo = models.ForeignKey(Vehiculo, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.nombre} → {self.vehiculo.patente}"
