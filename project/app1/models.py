from django.db import models

# Create your models here.
class Person(models.Model):
    nombre = models.CharField(max_length=255)


class Actor(models.Model):
    nombre = models.CharField(max_length=255)

    def __str__(self):
        return self.nombre


class Pelicula(models.Model):
    titulo = models.CharField(max_length=255)
    actores = models.ManyToManyField(Actor)

    def __str__(self):
        return self.titulo