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
        help_texts = {k:"" for k in fields}



