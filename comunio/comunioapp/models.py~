from django.db import models

# Create your models here.

class Equipo(models.Model):
	nombre = models.CharField(max_length=30)
	descripcion = models.TextField()

	def __str__(self):
		return '%s' % (self.nombre)

class Jugadores(models.Model):
	nombre = models.CharField(max_length=30)
	edad = models.IntegerField(null=True)
	equipo = models.ForeignKey('Equipo',null=True)
	
	def __str__(self):
		return '%s' % (self.nombre)
