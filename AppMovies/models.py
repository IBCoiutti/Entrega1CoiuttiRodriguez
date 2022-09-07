from django.db import models

# Create your models here.

class Pelicula(models.Model):
    nombre = models.CharField(max_length=70)
    director = models.CharField(max_length=50)
    año = models.IntegerField()
    genero = models.CharField(max_length=30)

class Serie(models.Model):
    nombre = models.CharField(max_length=70)
    director = models.CharField(max_length=50)
    año = models.IntegerField()
    genero = models.CharField(max_length=30)
    temporadas = models.IntegerField()

class Actores(models.Model):
    nombre = models.CharField(max_length=70)
    director = models.CharField(max_length=50)
    año = models.IntegerField()
    genero = models.CharField(max_length=30)
    temporadas = models.IntegerField()