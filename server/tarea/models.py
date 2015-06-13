from django.db import models
from animal.models import Animal

# Create your models here.
class Tarea (models.Model):
    nombre = models.CharField(max_length=80)
    animal = models.ForeignKey(Animal)
    descripcion = models.TextField(null=True, blank=True)
    fecha = models.DateTimeField(null=True, blank=True)

    def __unicode__(self):
        return unicode("Tarea: " + self.nombre + " con " + self.animal.nombre)

    def __str__(self):
        return "Tarea: " + self.nombre + " con " + self.animal.nombre
