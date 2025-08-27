from django.db import models

class Mecanico(models.Model):
    nombre = models.CharField(max_length=100)
    contacto = models.CharField(max_length=100)
    especialidad = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.nombre} ({self.especialidad})"
