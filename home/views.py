from django.shortcuts import render, redirect
from django.http import HttpResponse
from datetime import datetime
from home.models import Auto
from home.forms import CrearAuto, BuscarAuto
# Create your views here.


def home(request):
    #return HttpResponse("<h1>El inicio de Home</h1>")
    return render(request, 'home.html')

def saludo(request, nombre, apellido):
    hora_actual = datetime.now()
    return render(request, 'saludo.html', {'hora':hora_actual, 'nombre': nombre, 'apellido': apellido})

def crear_auto(request):
    print(request.GET)
    print(request.POST)
    formulario = CrearAuto()
    
    if request.method == "POST":
        formulario = CrearAuto(request.POST)
        if formulario.is_valid():
            marca = formulario.cleaned_data.get('marca')
            modelo = formulario.cleaned_data.get('modelo')
            descripcion = formulario.cleaned_data.get('descripcion')
            
            auto = Auto(marca=marca, modelo=modelo, descripcion=descripcion)
            auto.save()
            return redirect("listado_de_autos")
            
    return render(request, 'crear_auto.html', {"formulario": formulario})


def listado_de_autos(request):
    autos = Auto.objects.all()
    formulario = BuscarAuto(request.GET)
    if formulario.is_valid():
        modelo_a_buscar = formulario.cleaned_data.get("modelo")
        autos = Auto.objects.filter(modelo__icontains=modelo_a_buscar)
        
    return render(request, "listado_de_autos.html", {"autos": autos, "formulario": formulario})