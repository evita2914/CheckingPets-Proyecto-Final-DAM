from django.db import models

# Create your models here.
from animal.models import Animal

class Vacuna (models.Model):
    nombre = models.CharField(max_length=60)
    animal = models.ForeignKey(Animal)

    def __unicode__(self):
        return unicode(self.nombre + " de " + self.animal.nombre)

    def __str__(self):
        return self.nombre + " de " + self.animal.nombre

    def fechas(self):
        return FechaVacuna.objects.filter(vacuna=self)

class FechaVacuna (models.Model):
    fecha = models.DateField()
    vacuna = models.ForeignKey(Vacuna)

    def __unicode__(self):
        return unicode(self.vacuna) + u" el " + unicode(self.fecha.isoformat())

    def __str__(self):
        return self.vacuna.__str__() + " el " + self.fecha.isoformat()