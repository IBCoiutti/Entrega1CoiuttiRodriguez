from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Pelicula(models.Model):
    nombre = models.CharField(max_length=70)
    director = models.CharField(max_length=50)
    año = models.IntegerField()
    genero = models.CharField(max_length=30)

    def __str__(self):
        return self.nombre

class Serie(models.Model):
    nombre = models.CharField(max_length=70)
    director = models.CharField(max_length=50)
    año = models.IntegerField()
    genero = models.CharField(max_length=30)
    temporadas = models.IntegerField()

    def __str__(self):
        return self.nombre

class Actores(models.Model):
    nombre = models.CharField(max_length=70)
    director = models.CharField(max_length=50)
    año = models.IntegerField()
    genero = models.CharField(max_length=30)
    temporadas = models.IntegerField()

    def __str__(self):
        return self.nombre

class Avatar(models.Model):
    user=models.ForeignKey(User, on_delete=models.CASCADE)
    imagen= models.ImageField(upload_to='avatares')