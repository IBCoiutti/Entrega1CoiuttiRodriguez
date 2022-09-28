from django.http.request import QueryDict
from http.client import HTTPResponse
from django.shortcuts import render
from django.http import HttpResponse
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

"""def formPelicula(request):
    return render(request,"AppMovies/formulariopelicula.html")"""
    

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

    #respuesta = f"Buscar pelicula: {request.GET['nombre']}"

    if request.GET["nombre"]:

        nombre = request.GET['nombre']
        pelicula = Pelicula.objects.filter(nombre__icontains=nombre)

        return render(request, "AppMovies/resultadosbusqueda.html", {"nombre": nombre})

    else:
        respuesta = "No enviaste datos"

    
    return HttpResponse(respuesta)
