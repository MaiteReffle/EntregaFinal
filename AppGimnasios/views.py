from cmath import log
from math import remainder
from django.http import HttpResponse
from django.template import loader
from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView, TemplateView
from django.urls import reverse_lazy
from AppGimnasios.models import *
from AppGimnasios.forms import *
from django.contrib.auth.forms import AuthenticationForm #LOGIN
from django.contrib.auth import login, authenticate
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required

def sucursales(request):
    sucursales = Sucursales.objects.all()
    contexto = {"sucursales":sucursales}

    return render (request,'AppGimnasios/sucursales.html',contexto)
    
def horarios(request):
    horarios = Horarios.objects.all()
    contexto = {"horarios":horarios}

    return render (request,'AppGimnasios/horarios.html',contexto)

def inicio(request):
    return render(request,'AppGimnasios/inicio.html')

@login_required
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

@login_required
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

@login_required
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

def profesores(request):
    profesores = Profesores.objects.all()
    contexto = {"profesores":profesores}

    return render (request,'AppGimnasios/profesores.html',contexto)

class ProfesoresDelete(LoginRequiredMixin,DeleteView):
    model = Profesores
    success_url = reverse_lazy('Profesores')

@login_required
def editarProfesor(request,id):
    profesor = Profesores.objects.get(id = id)
    if request.method == 'POST':
        formulario = ProfesoresFormulario(request.POST)
        if formulario.is_valid():
            informacion = formulario.cleaned_data
            profesor.nombreProfesor = informacion['nombreProfesor']
            profesor.apellidoProfesor = informacion['apellidoProfesor']
            profesor.nombreClaseProfesor = informacion['nombreClaseProfesor']
            profesor.fechaDeNacimientoProfesor = informacion['fechaDeNacimientoProfesor']
            profesor.save()
            
            profesores = Profesores.objects.all()
            contexto = {'profesores': profesores}
            return render (request,'AppGimnasios/profesores.html',contexto)

    else:
        formulario = ProfesoresFormulario(initial={'id':profesor.id,'nombreProfesor':profesor.nombreProfesor,'apellidoProfesor':profesor.apellidoProfesor,'nombreClaseProfesor':profesor.nombreClaseProfesor,'fechaDeNacimientoProfesor':profesor.fechaDeNacimientoProfesor})
        contexto = {'formulario':formulario,'id':id}
        return render (request,'AppGimnasios/editarProfesor.html',contexto)

class ProfesoresDetail(LoginRequiredMixin,DetailView):
    model = Profesores
    template_name = 'AppGimnasios/profesoresDetalle.html'


class ClasesList(ListView):
    model = Clases
    template_name = 'AppGimnasios/clases.html'

class ClasesDetail(DetailView):
    model = Clases
    template_name = 'AppGimnasios/clasesDetalle.html'

class ClasesCreate(LoginRequiredMixin,CreateView):
    model = Clases
    success_url = reverse_lazy('Clases_list')
    fields = ['nombreClase','sucursalClase','profesorClase']


class ClasesUpdate(LoginRequiredMixin,UpdateView):
    model = Clases
    success_url = reverse_lazy('Clases_list')
    fields = ['nombreClase','sucursalClase','profesorClase']

class ClasesDelete(LoginRequiredMixin,DeleteView):
    model = Clases
    success_url = reverse_lazy('Clases_list')
  
#_____________________________________
#LOGIN
#_____________________________________
def login_request(request):
    if request.method == 'POST':
        form = AuthenticationForm(request,request.POST)
        if form.is_valid():
            usuario = form.cleaned_data.get('username')
            clave = form.cleaned_data.get('password')
    #Autenticación del usuario
            user = authenticate(username= usuario,password=clave)
            if user is not None:
                login(request,user)
                return render(request,'AppGimnasios/inicio.html')
            else: 
                return render(request,'AppGimnasios/inicio.html',{'aviso':'Usuario o contraseña incorrectos'})
        else: 
            return render(request,'AppGimnasios/inicio.html',{'error':'Error. El formulario es inválido'})
    else:
        form = AuthenticationForm()
        contexto = {'form':form}
        return render(request,'AppGimnasios/login.html',contexto)

#_____________________________________
#REGISTER
#_____________________________________
def register_request(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            form.save()
            return render (request,'AppGimnasios/inicio.html',{'mensaje': f'Usuario {username} creado'})
        else:
            return render (request,'AppGimnasios/inicio.html',{'mensaje': f'Error. No se pudo crear el usuario'})
    else:
        form = UserRegistrationForm()
        contexto = {'form':form}
        return render (request,'AppGimnasios/register.html',contexto)

#_____________________________________
#EDITPROFILE
#_____________________________________
@login_required
def editarPerfil(request):
    usuario = request.user

    if request.method == 'POST':
        formularioPerfil = UserEditForm(request.POST, instance=usuario)
        if formularioPerfil.is_valid():
            informacion = formularioPerfil.cleaned_data
            usuario.email = informacion['email']
            usuario.password1 = informacion['password1']
            usuario.password2 = informacion['password2']

            return render(request,'AppGimnasios/inicio.html',{'mensaje':'Datos modificados con éxito'})
    else:
        formularioPerfil = UserEditForm(instance = usuario)
    return render(request,'AppGimnasios/editarPerfil.html',{'usuario':usuario.username,'formularioPerfil':formularioPerfil})

class VerPerfil(ListView):
    model = User
    template_name = 'AppGimnasios/verPerfil.html'


#_____________________________________
#Blog
#_____________________________________

class BlogCreate(LoginRequiredMixin,CreateView):
    model = Blog
    success_url = reverse_lazy('blog')
    fields = ['titulo','subtitulo','cuerpo','owner']

class BlogList(ListView):
    model = Blog
    template_name = 'AppGimnasios/blog.html'

class BlogDetail(DetailView):
    model = Blog
    template_name = 'AppGimnasios/blogDetalle.html'

class BlogUpdate(LoginRequiredMixin,UpdateView):
    model = Blog
    success_url = reverse_lazy('blog')
    fields = ['titulo','subtitulo','cuerpo','owner']


class BlogDelete(LoginRequiredMixin,DeleteView):
    model = Blog
    success_url = reverse_lazy('blog')

#ABOUT
def about(request):
    return render(request,'AppGimnasios/about.html')

#CAPTURAR ERROR 404
class Error404View(TemplateView):
    template_name = 'AppGimnasios/error404.html'
