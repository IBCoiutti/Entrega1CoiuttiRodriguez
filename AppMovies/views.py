from http.client import HTTPResponse
from django.shortcuts import render
from django.http import HttpResponse
from AppMovies.models import Pelicula, Serie, Actores


# Create your views here.

def pelicula(request):
    pelicula=Pelicula(nombre="star wars", director="George Lucas", año=1977, genero="ciencia ficcion")
    pelicula.save()
    texto=f"pelicula añadida:{pelicula.nombre}"
    return HttpResponse(texto)

def inicio(request):
    return render (request,"AppMovies/inicio.html")

def peliculas(request):
    return render (request,"AppMovies/peliculas.html")

def series(request):
    return render (request,"AppMovies/series.html")

def actores(request):
    return render (request,"AppMovies/actores.html")