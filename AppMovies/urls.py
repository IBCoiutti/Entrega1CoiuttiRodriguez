from django.contrib import admin
from django.urls import path
from AppMovies.views import *


urlpatterns = [
    path('peliculas/', peliculas),
    path('inicio/', inicio, name="inicio"),
    path('actores/', actores),
    path('series/', series),
    path("", inicio),
]
