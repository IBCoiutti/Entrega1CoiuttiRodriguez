from django.contrib import admin
from django.urls import path
from AppMovies.views import *



urlpatterns = [
    path('peliculas/', peliculas, name="peliculas"),
    path('inicio/', inicio, name="inicio"),
    path('actores/', actores, name="actores"),
    path('series/', series, name="series"),
    path("", inicio),
    path('formulariopelicula/', formPelicula, name="formulariopelicula"),
    path('buscarpelicula/', buscarPeli, name="buscarpelicula"),
    path('buscar/', buscar, name="buscar"),
    path('todaslaspeliculas/', pelisTodas, name="todaslaspeliculas"),
    path('eliminarpeli/<id>', eliminarPeli, name="eliminarPeli"),
    path('editarpelicula/<id>', editarPeli, name="editarPeli"),
]

