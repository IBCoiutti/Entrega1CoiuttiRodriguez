from dataclasses import field, fields
from socket import fromshare
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class PeliForm(forms.Form):
    nombre = forms.CharField(max_length=70)
    director = forms.CharField(max_length=50)
    año = forms.IntegerField()
    genero = forms.CharField(max_length=30)

class UserRegisterForm(UserCreationForm):
    email = forms.EmailField()
    password1= forms.CharField(label="Ingrese Contraseña", widget=forms.PasswordInput)
    password2= forms.CharField(label="Confirme Contraseña", widget=forms.PasswordInput)

    class meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']
        #help_texts = {k:"" for k in fields} esto lo hice desde el html por que me quedaba algo siempre
        help_texts = {'username': None,'email': None,'password1': None, 'password2': None}


class UserEditForm(UserCreationForm):
    email = forms.EmailField()
    password1= forms.CharField(label="Ingrese Contraseña", widget=forms.PasswordInput)
    password2= forms.CharField(label="Confirme Contraseña", widget=forms.PasswordInput)
    first_name=forms.CharField(label='Modificar Nombre')
    last_name=forms.CharField(label='Modificar Apellido')

    class meta:
        model = User
        fields = ['email', 'password1', 'password2', 'first_name', 'last_name'] #borré el username y no deja de mostrarmelo.
        #help_texts = {k:"" for k in fields} esto lo hice desde el html por que me quedaba algo siempre
        help_texts = {k:"" for k in fields}


class AvatarForm(forms.Form):
    imagen= forms.ImageField(label="Imagen")