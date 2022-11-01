from re import template
from django.contrib import admin
from django.urls import path
from AppMovies.views import *
from django.contrib.auth.views import LogoutView 



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


    #loggin register logout
    path('login/', login_request, name="login"),
    path('register/', register, name="register"),
    path('logout/', LogoutView.as_view(template_name='AppMovies/logout.html'), name='logout'),
    path('editarusuario/', editarUsuario, name="editarusuario"),
    path('agregaravatar/', agregarAvatar, name='agregaravatar'),
]

