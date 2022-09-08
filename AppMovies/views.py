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
    return HttpResponse ("Peliculas")

def series(request):
    return HttpResponse ("Series")

def actores(request):
    return HttpResponse ("Actores")