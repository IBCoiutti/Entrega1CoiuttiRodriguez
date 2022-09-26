from http.client import HTTPResponse
from django.shortcuts import render
from django.http import HttpResponse
from AppMovies.forms import PeliForm
from AppMovies.models import Pelicula, Serie, Actores
from AppMovies.forms import PeliForm

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

def formPelicula(request):
    return render(request,"AppMovies/formulariopelicula.html")
    

def peliFormulario(request):
    if request.method=="POST":
        pass
    else:
        formulario = PeliForm(request.POST)
        return render (request,"AppMovies/pelisFormulario.html", {"formulario": formulario})