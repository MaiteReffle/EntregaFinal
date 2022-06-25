from django.urls import path
from AppGimnasios import views

urlpatterns = [
    path('',views.inicio,name='Inicio'),
    path('sucursales/',views.sucursales, name='Sucursales'),
    path('profesores/',views.profesores,name='Profesores'),
    path('horarios/',views.horarios,name='Horarios'),

#URLs formularios
    path('sucursalesFormulario/',views.sucursalesFormulario,name='sucursalesFormulario'),
    path('profesoresFormulario/',views.profesoresFormulario,name='profesoresFormulario'),
    path('clasesFormulario/',views.clasesFormulario,name='clasesFormulario'),
    path('horariosFormulario/',views.horariosFormulario,name='horariosFormulario'),

#URLS para GET y POST
    path('busquedaSucursal/',views.busquedaSucursal,name='busquedaSucursal'),
    path('buscarSucursal/',views.buscarSucursal,name='buscarSucursal'),

#URLS de CRUD manual
    path('eliminarProfesor/<id>',views.eliminarProfesor,name='eliminarProfesor'),
    path('editarProfesor/<id>',views.editarProfesor,name='editarProfesor'),

#URLs de CRUD DJANGO
    path('clases/list/',views.ClasesList.as_view(),name='Clases_list'),
    path('clases/<pk>',views.ClasesDetail.as_view(),name='Clases_detail'),
    path('clases/new/',views.ClasesCreate.as_view(),name='Clases_create'),
    path('clases/update/<pk>',views.ClasesUpdate.as_view(),name='Clases_update'),
    path('clases/delete/<pk>',views.ClasesDelete.as_view(),name='Clases_delete'),
]