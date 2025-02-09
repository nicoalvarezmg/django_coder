from django.shortcuts import render
from django.http import HttpResponse
from datetime import datetime
# Create your views here.


def home(request):
    #return HttpResponse("<h1>El inicio de Home</h1>")
    return render(request, 'home.html')

def saludo(request, nombre, apellido):
    hora_actual = datetime.now()
    return render(request, 'saludo.html', {'hora':hora_actual, 'nombre': nombre, 'apellido': apellido})