from django.contrib import admin
from django.urls import path
from AppMovies.views import *



urlpatterns = [
    path('peliculas/', peliculas),
    path('inicio/', inicio, name="inicio"),
    path('actores/', actores, name="actores"),
    path('series/', series, name="series"),
    path("", inicio),
]
