from django.contrib.auth.models import User
from django.db import models
from easy_thumbnails.fields import ThumbnailerImageField
from animal.settings import COLORES_CHOICES


class TipoAnimal(models.Model):
	nombre = models.CharField(max_length=40)

	def __unicode__(self):
		return unicode(self.nombre)

	def __str__(self):
		return self.nombre


class Animal(models.Model):
	amo = models.ForeignKey(User, blank=True, null=True)
	nombre = models.CharField(max_length=40)
	nacimiento = models.DateField(null=True, blank=True)
	descripcion = models.TextField(null=True, blank=True)
	foto = ThumbnailerImageField(upload_to='fotos/', blank=True)
	color = models.IntegerField(default=0, choices=COLORES_CHOICES)
	tipo = models.ForeignKey(TipoAnimal)

	def __unicode__(self):
		return unicode(self.nombre + " el " + self.tipo.nombre)

	def __str__(self):
		return self.nombre + " el " + self.tipo.nombre

	def get_verbose_color(self):
		return self.get_color_display()