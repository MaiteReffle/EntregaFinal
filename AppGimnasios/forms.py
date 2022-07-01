from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from tinymce import models as tinymce_forms
from .models import Blog

class SucursalesFormulario(forms.Form):
    nombreSucursal=forms.CharField(max_length=40)
    direccionSucursal=forms.CharField(max_length=40)
    fechaDeInauguracionSucursal=forms.DateField()

class ClasesFormulario(forms.Form):
    nombreClase=forms.CharField(max_length=40)

class ProfesoresFormulario(forms.Form):
    nombreProfesor=forms.CharField(max_length=40)
    apellidoProfesor=forms.CharField(max_length=40)
    nombreClaseProfesor=forms.CharField(max_length=60)
    fechaDeNacimientoProfesor=forms.DateField()

class HorariosFormulario(forms.Form):
    nombreClaseH=forms.CharField(max_length=40)
    horarioClase=forms.TimeField()


class BlogFormulario(forms.ModelForm):
    titulo=forms.CharField(max_length=40)
    subtitulo=forms.CharField(max_length=40)
    cuerpo=tinymce_forms.HTMLField()
    
    class Meta:
        model = Blog
        fields = ['titulo','subtitulo','cuerpo']


class UserRegistrationForm(UserCreationForm):
    email = forms.EmailField(required=True)
    password1 = forms.CharField(label='Constraseña',widget=forms.PasswordInput)
    password2 = forms.CharField(label='Confirmar Constraseña',widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ['username','email','password1','password2']
        help_texts = {k:"" for k in fields}

class UserEditForm(UserCreationForm):
    email = forms.EmailField(required=False)
    last_name = forms.CharField(label='Modificar apellido',required=False)
    first_name = forms.CharField(label='Modificar nombre',required=False)
    password1 = forms.CharField(label='Modificar constraseña',widget=forms.PasswordInput,required=False)
    password2 = forms.CharField(label='Confirmar nueva constraseña',widget=forms.PasswordInput,required=False)


    class Meta:
        model = User
        fields = ['email','first_name','last_name','password1','password2']
        help_texts = {k:"" for k in fields}

