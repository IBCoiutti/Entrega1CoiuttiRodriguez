from django.http.request import QueryDict
from http.client import HTTPResponse
from django.shortcuts import render
from django.http import HttpResponse
from AppMovies.models import Pelicula, Serie, Actores
from AppMovies.forms import PeliForm

# Create your views here.


def inicio(request):
    return render (request,"AppMovies/inicio.html")

def peliculas(request):
    return render (request,"AppMovies/peliculas.html")

def series(request):
    return render (request,"AppMovies/series.html")

def actores(request):
    return render (request,"AppMovies/actores.html")


def formPelicula(request):
    if request.method=="POST":
        Formulario1 = PeliForm(request.POST) #aquí mellega toda la información del html

        print(Formulario1)

        if Formulario1.is_valid:   #Si pasó la validación de Django

            informacion = Formulario1.cleaned_data

            peli = Pelicula (nombre=informacion['nombre'], director=informacion['director'], año=informacion['año'], genero=informacion['genero'])

            peli.save()

            return render(request, "AppMovies/inicio.html") #Vuelvo al inicio o a donde quieran
    else:
        
        Formulario1 = PeliForm()

    return render (request,"AppMovies/formulariopelicula.html", {"Formulario1": Formulario1})




def buscarPeli(request):

    return render(request, "AppMovies/buscarpelicula.html")



def buscar(request):

    request.GET["nombre"]
    titulo = request.GET["nombre"]
    titulos = Pelicula.objects.filter(nombre=titulo)
    return render(request,"AppMovies/resultadosporbusqueda.html", {"titulos":titulos})

    




    





