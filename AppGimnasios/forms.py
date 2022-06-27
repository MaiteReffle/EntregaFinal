from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

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

class UserRegistrationForm(UserCreationForm):
    email = forms.EmailField(required=True)
    password1 = forms.CharField(label='Constraseña',widget=forms.PasswordInput)
    password2 = forms.CharField(label='Confirmar Constraseña',widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ['username','email','password1','password2']
        help_texts = {k:"" for k in fields}