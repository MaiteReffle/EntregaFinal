from math import remainder
from django.http import HttpResponse
from django.template import loader
from django.shortcuts import render
from AppGimnasios.models import *
from AppGimnasios.forms import *

def sucursales(request):
    return render(request,'appGimnasios/sucursales.html')

def clases(request):
    return render(request,'appGimnasios/clases.html')

def profesores(request):
    return render(request,'appGimnasios/profesores.html')

def horarios(request):
    return render(request,'appGimnasios/horarios.html')

def inicio(request):
    return render(request,'appGimnasios/inicio.html')

def sucursalesFormulario(request):
    if request.method == 'POST':
        formularioSucursal = SucursalesFormulario(request.POST)
        if formularioSucursal.is_valid():
            informacionSucursal = formularioSucursal.cleaned_data
        nombreSucursal=informacionSucursal['nombreSucursal']
        direccionSucursal=informacionSucursal['direccionSucursal']
        fechaDeInauguracionSucursal=informacionSucursal['fechaDeInauguracionSucursal']
        sucursal = Sucursales(nombreSucursal=nombreSucursal,direccionSucursal=direccionSucursal,fechaDeInauguracionSucursal=fechaDeInauguracionSucursal)
        sucursal.save()
        return render(request,'AppGimnasios/inicio.html')

    else:
        formularioSucursal = SucursalesFormulario()
    return render(request,'AppGimnasios/sucursalesFormulario.html', {'formularioSucursal':formularioSucursal})

def profesoresFormulario(request):
    if request.method == 'POST':
        formularioProfesor = ProfesoresFormulario(request.POST)
        if formularioProfesor.is_valid():
            informacionProfesor = formularioProfesor.cleaned_data
        nombreProfesor=informacionProfesor['nombreProfesor']
        apellidoProfesor=informacionProfesor['apellidoProfesor']
        nombreClaseProfesor=informacionProfesor['nombreClaseProfesor']
        fechaDeNacimientoProfesor=informacionProfesor['fechaDeNacimientoProfesor']
        profesor = Profesores(nombreProfesor=nombreProfesor,apellidoProfesor=apellidoProfesor,nombreClaseProfesor=nombreClaseProfesor,fechaDeNacimientoProfesor=fechaDeNacimientoProfesor)
        profesor.save()
        return render(request,'AppGimnasios/inicio.html')

    else:
        formularioProfesor = ProfesoresFormulario()
    return render(request,'AppGimnasios/profesoresFormulario.html', {'formularioProfesor':formularioProfesor}) 

def clasesFormulario(request):
    if request.method == 'POST':
        formularioClase = ClasesFormulario(request.POST)
        if formularioClase.is_valid():
            informacionClase = formularioClase.cleaned_data
        nombreClase=informacionClase['nombreClase']
        clases = Clases(nombreClase=nombreClase)
        clases.save()
        return render(request,'AppGimnasios/inicio.html')

    else:
        formularioClase = ClasesFormulario()
    return render(request,'AppGimnasios/clasesFormulario.html', {'formularioClase':formularioClase}) 

def horariosFormulario(request):
    if request.method == 'POST':
        formularioHorario = HorariosFormulario(request.POST)
        if formularioHorario.is_valid():
            informacionHorario = formularioHorario.cleaned_data
        nombreClaseH=informacionHorario['nombreClaseH']
        horarioClase=informacionHorario['horarioClase']
        horarios = Horarios(nombreClaseH=nombreClaseH,horarioClase=horarioClase)
        horarios.save()
        return render(request,'AppGimnasios/inicio.html')

    else:
        formularioHorario = HorariosFormulario()
    return render(request,'AppGimnasios/horariosFormulario.html', {'formularioHorario':formularioHorario}) 


def busquedaSucursal(request):
    return render(request,'AppGimnasios/busquedaSucursal.html')

def buscarSucursal(request):
    if request.GET['nombreSucursal']:
        nombreSucursal = request.GET['nombreSucursal']
        sucursales = Sucursales.objects.filter(nombreSucursal=nombreSucursal)
        return render(request,'AppGimnasios/resultadosBusquedaSucursal.html', {'sucursales':sucursales, 'nombreSucursal':nombreSucursal})
    else: 
        respuesta = "No se ha ingresado sucursal válida"
    return render(request,'AppGimnasios/resultadosBusquedaSucursal.html', {"respuesta":respuesta})

