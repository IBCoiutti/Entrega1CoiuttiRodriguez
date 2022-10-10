import re
from django.http.request import QueryDict
from http.client import HTTPResponse
from django.shortcuts import render
from django.http import HttpResponse
from django.urls import is_valid_path
from AppMovies.models import Pelicula, Serie, Actores
from AppMovies.forms import PeliForm
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, logout, authenticate


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
            todas=Pelicula.objects.all()
            return render(request, "AppMovies/todaslaspeliculas.html", {"todas":todas})

    else:
        
        Formulario1 = PeliForm()

    return render (request,"AppMovies/formulariopelicula.html", {"Formulario1": Formulario1})

def buscarPeli(request):

    return render(request, "AppMovies/buscarpelicula.html")

def buscar(request):
    if request.GET["nombre"]:
        request.GET["nombre"]
        titulo = request.GET["nombre"]
        titulos = Pelicula.objects.filter(nombre=titulo)
        return render(request,"AppMovies/resultadosporbusqueda.html", {"titulos":titulos})
    else:
        return render(request, "AppMovies/buscarpelicula.html", {"mensaje":"Ingresar un titulo"})

def pelisTodas(request):
    todas=Pelicula.objects.all()
    return render(request, "AppMovies/todaslaspeliculas.html", {"todas":todas})

def eliminarPeli(request, id):
    peli=Pelicula.objects.get(id=id)
    peli.delete()
    todas=Pelicula.objects.all()
    return render(request, "AppMovies/todaslaspeliculas.html", {"todas": todas})

def editarPeli(request, id):
    peli=Pelicula.objects.get(id=id)
    if request.method=="POST":
        form=PeliForm(request.POST)
        if form.is_valid():
            info=form.cleaned_data
            peli.nombre=info["nombre"]
            peli.director=info["director"]
            peli.año=info["año"]
            peli.genero=info["genero"]
            peli.save()
            todas=Pelicula.objects.all()
            return render(request, "AppMovies/todaslaspeliculas.html", {"todas": todas})
    else:
        form= PeliForm(initial={"nombre": peli.nombre, "director": peli.director, "año": peli.año, "genero": peli.genero})
        return render(request, "AppMovies/editarpelicula.html", {"Formulario1": form, "peli":peli})

#Login

def login_request(request):
    if request.method=="POST":
        form=AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            usu=request.POST["username"]
            clave=request.POST["password"]

            usuario = authenticate(username=usu, password=clave)
            if usuario is not None:
                login(request, usuario)
                return render(request, "AppMovies/inicio.html", {'mensaje':f"Bienvenido {usuario}!"} )
            
            else:
                return render (request, "AppMovies/login.html",{"Formulario1":form, 'mensaje': "Usuario o contraseña incorrectos"})
        else:
            return render (request, "AppMovies/login.html",{"Formulario1":form, 'mensaje': "Usuario y/o contraseña incorrectos"})


    else:
        form=AuthenticationForm()
        return render (request, "AppMovies/login.html",{"Formulario1":form})



    




    



