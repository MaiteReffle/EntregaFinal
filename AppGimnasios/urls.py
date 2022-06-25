from django.urls import path
from AppGimnasios import views

urlpatterns = [
    path('',views.inicio,name='Inicio'),
    path('sucursales/',views.sucursales, name='Sucursales'),
    path('clases/',views.clases,name='Clases'),
    path('profesores/',views.profesores,name='Profesores'),
    path('horarios/',views.horarios,name='Horarios'),
    path('sucursalesFormulario/',views.sucursalesFormulario,name='sucursalesFormulario'),
    path('profesoresFormulario/',views.profesoresFormulario,name='profesoresFormulario'),
    path('clasesFormulario/',views.clasesFormulario,name='clasesFormulario'),
    path('horariosFormulario/',views.horariosFormulario,name='horariosFormulario'),
    path('busquedaSucursal/',views.busquedaSucursal,name='busquedaSucursal'),
    path('buscarSucursal/',views.buscarSucursal,name='buscarSucursal'),
]