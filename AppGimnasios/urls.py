from re import template
from django import urls
from django.urls import path
from AppGimnasios import views
from django.contrib.auth.views import LogoutView
from django.conf.urls import *
from django.conf import settings
from django.contrib import admin
admin.autodiscover()


urlpatterns = [
    path('',views.inicio,name='Inicio'),
    path('sucursales/',views.sucursales, name='Sucursales'),
    path('profesores/',views.profesores,name='Profesores'),
    path('horarios/',views.horarios,name='Horarios'),

#URLs formularios manuales
    path('sucursalesFormulario/',views.sucursalesFormulario,name='sucursalesFormulario'),
    path('profesoresFormulario/',views.profesoresFormulario,name='profesoresFormulario'),
    path('horariosFormulario/',views.horariosFormulario,name='horariosFormulario'),

#URLS para GET y POST
    path('busquedaSucursal/',views.busquedaSucursal,name='busquedaSucursal'),
    path('buscarSucursal/',views.buscarSucursal,name='buscarSucursal'),

#URLS de CRUD manual
    path('editarProfesor/<id>',views.editarProfesor,name='editarProfesor'),

#URLs de CRUD DJANGO
    path('clases/list/',views.ClasesList.as_view(),name='Clases_list'),
    path('clases/<pk>',views.ClasesDetail.as_view(),name='Clases_detail'),
    path('clases/new/',views.ClasesCreate.as_view(),name='Clases_create'),
    path('clases/update/<pk>',views.ClasesUpdate.as_view(),name='Clases_update'),
    path('clases/delete/<pk>',views.ClasesDelete.as_view(),name='Clases_delete'),
    path('profesores/<pk>',views.ProfesoresDetail.as_view(),name='Profesores_detail'),
    path('profesores/delete/<pk>',views.ProfesoresDelete.as_view(),name='Profesores_delete'),

#LOGIN, REGISTER, LOGOUT y EDITPROFILE
    path('cuenta/login',views.login_request,name='login'),
    path('cuenta/signup',views.register_request,name='register'),
    path('cuenta/logout',LogoutView.as_view(template_name = 'AppGimnasios/logout.html'),name='logout'),
    path('cuenta/perfil',views.VerPerfil.as_view(),name='verPerfil'),
    path('cuenta/editarPerfil',views.editarPerfil,name='editarPerfil'),

#BLOG
    path('blog/pages',views.BlogList.as_view(),name='blog'),
    path('blog/new/',views.BlogCreate.as_view(),name='blog_create'),
    path('blog/pages/<pk>',views.BlogDetail.as_view(),name='blog_detail'),
    path('blog/update/<pk>',views.BlogUpdate.as_view(),name='blog_update'),
    path('blog/delete/<pk>',views.BlogDelete.as_view(),name='blog_delete'),
    
    path('tinymce/', include('tinymce.urls')),

#ABOUT
    path('about/',views.about,name='about'),
]