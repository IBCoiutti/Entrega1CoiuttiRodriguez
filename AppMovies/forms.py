from socket import fromshare
from django import forms


class PeliForm(forms.Form):
    nombre = forms.CharField(max_length=70)
    director = forms.CharField(max_length=50)
    año = forms.IntegerField()
    genero = forms.CharField(max_length=30)


